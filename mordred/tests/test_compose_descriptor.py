from .. import ABCIndex
from nose.tools import eq_
from rdkit import Chem

import operator
import math


binary = [
    operator.add,
    operator.sub,
    operator.mul,
    operator.truediv,
    operator.floordiv,
    operator.mod,
    operator.pow,
]

unary = [
    operator.neg,
    operator.pos,
    operator.abs,

    math.ceil,
    math.floor,
    math.trunc,
]


def test_compose_descriptor():
    l = ABCIndex.ABCIndex()
    r = ABCIndex.ABCGGIndex()
    m = Chem.MolFromSmiles('c1ccccc1C')

    for op in binary:
        yield eq_, op(l, r)(m), op(l(m), r(m))

    for op in unary:
        yield eq_, op(l)(m), op(l(m))
