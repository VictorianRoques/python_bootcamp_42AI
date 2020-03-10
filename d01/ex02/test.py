from vector import Vector
v1 = Vector((10,15))
v2 = Vector((0,5))

v3 = v1.__sub__(v2)
v4 = v1 / 2
v5 = v4 * 2
print(v5)
somme = v5 * v2
print(somme)