from googletrans import Translator
x=Translator()
tex1 = input("enter any sentence:")
tex2 = input("enter target language:")
res=x.translate(tex1,dest=tex2)
print("the original:",tex1)
print("Translate :",res)

