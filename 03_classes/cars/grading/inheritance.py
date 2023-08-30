#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here

from abc import ABC
import ast

Car = grading_import("task.combustion_car", "Car")
CombustionCar = grading_import("task.combustion_car", "CombustionCar")
ElectricCar = grading_import("task.electric_car", "ElectricCar")
HybridCar = grading_import("task.hybrid_car", "HybridCar")

ANNO = "abstractmethod"

class TestInheritance(AccessTestCase):

    @marks(1)
    def test_car(self):
        try:
            sut = TestCar()
        except:
            m = "Anonymous subclass of Car cannot be instantiated."
            self.fail(m)
        self.assertIsInstance(sut, ABC, "Car does not extend ABC.")

    @marks(1)
    def test_electric_car(self):
        try:
            sut = ElectricCar(1.0, 2.0)
        except:
            m = "ElectricCar cannot be instantiated."
            self.fail(m)
        self.assertIsInstance(sut, Car, "ElectricCar does not extend Car.")

    @marks(1)
    def test_combustion_car(self):
        try:
            sut = CombustionCar(1.0, 2.0)
        except:
            m = "CombustionCar cannot be instantiated."
            self.fail(m)
        self.assertIsInstance(sut, Car, "CombustionCar does not extend Car.")

    @marks(1)
    def test_hybrid_car(self):
        try:
            sut = HybridCar(1.0, 2.0, 3.0, 4.0)
        except:
            m = "HybridCar cannot be instantiated."
            self.fail(m)
        self.assertIsInstance(sut, Car, "HybridCar does not extend Car.")
        self.assertIsInstance(sut, ElectricCar, "HybridCar does not extend ElectricCar.")
        self.assertIsInstance(sut, CombustionCar, "HybridCar does not extend CombustionCar.")

    @marks(1)
    def test_for_abstract_method_annotations(self):
        with open("task/car.py") as f:
            tree = ast.parse(f.read())

            #print(ast.dump(tree))

            v = ABCTestVisitor()
            v.visit(tree)

            for name in ["drive", "get_remaining_range"]:
                if name not in v.annotated_methods:
                    m = "The method '{}' lacks the required annotation '{}'.".format(name, ANNO)
                    self.fail(m)


class ABCTestVisitor(ast.NodeVisitor):

    def __init__(self):
        self.annotated_methods = []

    def visit_FunctionDef(self, node):
        for d in node.decorator_list:
            if d.id == ANNO:
                self.annotated_methods.append(node.name)


class TestCar(Car):
    def get_remaining_range(self): pass
    def drive(self): pass