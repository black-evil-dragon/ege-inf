"""
Логическая операция 	Представление в Питоне
Отрицание ¬ 	        not()
Логическое умножение ∧ 	and
Логическое сложение ∨ 	or
Следование A ⟶ B 	    not(A) or B
Равносильность ≡ 	    ==


F --- False = 0 True = 1
"""


print('x y z w | F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (
                    (x == (w or y)) or ((not(w) or z) and (not(y) or w))
                )
                if not F:
                    print(x, y, z, w, '|', F)


