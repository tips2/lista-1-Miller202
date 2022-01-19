Queijo = False
Cheddar = False
Mussarela = False
Prato = False
Pizza_mussarela = False
Pizza_doisQueijos = False
Pizza_tresQueijos = False

def facts():
  global Queijo
  Queijo = True

if __name__ == "__main__":
  facts()
  lim = range(0, 10)
  for i in lim:
    if(Pizza_tresQueijos):
      Cheddar = True  

    if(Queijo and Prato):
      Pizza_tresQueijos = True

    if(Queijo and Mussarela):
      Pizza_mussarela = True

    if(Queijo):
      Mussarela = True
      Prato = True

    if(Pizza_mussarela and Cheddar):
      Pizza_doisQueijos = True

    if(Pizza_doisQueijos):
      print(f'(Pizza dois queijos) = Sim\n')
      break

  else:
    print(f'(Pizza dois queijos) = Não\n')