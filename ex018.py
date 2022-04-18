import math
an = (float (input('Digite o ângulo:')))
sen = math.sin (math.radians(an))
cos = math.cos (math.radians(an))
tan = math.tan (math.radians(an))
print ('O seno do ângulo {} é {:.2f}, o cosseno é: {:.2f} e a tangente é {:.2f}'.format (an, sen, cos, tan))

