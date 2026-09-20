"""以整数精确核对 AlphaEvolve 固定 notebook 的 4×4 rank-48 张量工件。

仅读取 JSON 与 Python AST 的数值字面量；绝不执行下载的 notebook 代码。
运行：python scripts/check_alphaevolve_rank48.py
"""

from __future__ import annotations

import ast
import hashlib
import json
import urllib.request
from fractions import Fraction


COMMIT = "9909c1347ea1b28d0c17dcb1f879a1c91b7dec3a"
URL = (
    "https://raw.githubusercontent.com/google-deepmind/alphaevolve_results/"
    f"{COMMIT}/mathematical_results.ipynb"
)
EXPECTED_SHA256 = "589ce95c3ff63ab2ea506e2e6ced44213d6e76f4bdb4b1b73e78d240bcc15008"

RationalGaussian = tuple[Fraction, Fraction]
GaussianInteger = tuple[int, int]


def _literal(node: ast.AST) -> RationalGaussian:
    """仅解读数值、正负号与加减；其余语法一律拒绝。"""
    if isinstance(node, ast.Constant):
        value = node.value
        if type(value) is int:
            return Fraction(value), Fraction(0)
        if type(value) is float:
            return Fraction.from_float(value), Fraction(0)
        if type(value) is complex:
            return Fraction.from_float(value.real), Fraction.from_float(value.imag)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        real, imag = _literal(node.operand)
        return (-real, -imag) if isinstance(node.op, ast.USub) else (real, imag)
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub)):
        left = _literal(node.left)
        right = _literal(node.right)
        sign = 1 if isinstance(node.op, ast.Add) else -1
        return left[0] + sign * right[0], left[1] + sign * right[1]
    raise ValueError(f"发现非允许的系数字面量语法：{ast.dump(node)[:120]}")


def _twice_gaussian_integer(node: ast.AST) -> GaussianInteger:
    real, imag = _literal(node)
    twice_real, twice_imag = 2 * real, 2 * imag
    if twice_real.denominator != 1 or twice_imag.denominator != 1:
        raise ValueError("系数不是实部和虚部均为半整数的复数")
    return int(twice_real), int(twice_imag)


def _is_np_attr(node: ast.AST, attr: str) -> bool:
    return (
        isinstance(node, ast.Attribute)
        and node.attr == attr
        and isinstance(node.value, ast.Name)
        and node.value.id == "np"
    )


def _read_factors(raw: bytes) -> list[list[list[GaussianInteger]]]:
    notebook = json.loads(raw)
    cell = "".join(notebook["cells"][36]["source"])
    module = ast.parse(cell)
    if len(module.body) != 1 or not isinstance(module.body[0], ast.Assign):
        raise ValueError("数据 cell 的顶层结构改变")
    assignment = module.body[0]
    if (
        len(assignment.targets) != 1
        or not isinstance(assignment.targets[0], ast.Name)
        or assignment.targets[0].id != "decomposition_444"
        or not isinstance(assignment.value, ast.Tuple)
        or len(assignment.value.elts) != 3
    ):
        raise ValueError("48 项分解的赋值结构改变")

    factors = []
    for call in assignment.value.elts:
        if (
            not isinstance(call, ast.Call)
            or not _is_np_attr(call.func, "array")
            or len(call.args) != 1
            or not isinstance(call.args[0], ast.List)
            or len(call.keywords) != 1
            or call.keywords[0].arg != "dtype"
            or not _is_np_attr(call.keywords[0].value, "complex64")
        ):
            raise ValueError("因子矩阵结构或 dtype 改变")
        rows = []
        for row in call.args[0].elts:
            if not isinstance(row, ast.List) or len(row.elts) != 48:
                raise ValueError("因子矩阵列数不是 48")
            rows.append([_twice_gaussian_integer(x) for x in row.elts])
        if len(rows) != 16:
            raise ValueError("因子矩阵行数不是 16")
        factors.append(rows)
    return factors


def _multiply(x: GaussianInteger, y: GaussianInteger) -> GaussianInteger:
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def main() -> None:
    with urllib.request.urlopen(URL, timeout=30) as response:
        raw = response.read()
    sha256 = hashlib.sha256(raw).hexdigest()
    if sha256 != EXPECTED_SHA256:
        raise ValueError(f"notebook SHA-256 与冻结工件不符：{sha256}")
    u, v, w = _read_factors(raw)

    checked = 0
    nonzero_targets = 0
    for a in range(16):
        for b in range(16):
            for c in range(16):
                # 行序 a=(i,j), b=(j',k), c=(k',i')。
                target = int(a // 4 == c % 4 and a % 4 == b // 4 and b % 4 == c // 4)
                nonzero_targets += target
                total = (0, 0)
                for rank in range(48):
                    term = _multiply(_multiply(u[a][rank], v[b][rank]), w[c][rank])
                    total = total[0] + term[0], total[1] + term[1]
                # 每个原系数乘 2，因此三因子乘积需与 2³T=8T 比较。
                expected = (8 * target, 0)
                if total != expected:
                    raise AssertionError((a, b, c, total, expected))
                checked += 1

    print(
        "ALPHAEVOLVE-RANK48-EXACT-CHECK: PASS "
        f"sha256={sha256} factors=3x16x48 coordinates={checked} "
        f"target_ones={nonzero_targets} arithmetic=Gaussian-integers"
    )


if __name__ == "__main__":
    main()
