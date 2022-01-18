Queijo = False
Pizza_queijo = False
Pizza_doisQueijos = False
Cheddar = False
Mussarela = False
Pizza_tresQueijos = False

def facts():
  global Queijo
  Queijo = True

if __name__ == "__main__":
  facts()
  lim = range(0, 10)
  for i in lim:
    if(Pizza_doisQueijos):
      print(f'(Pizza dois queijos) = Sim\n')
      break

    if(Pizza_queijo and Cheddar):
      Pizza_doisQueijos = True

    if(Queijo):
      Mussarela = True
      Pizza_tresQueijos = True

    if(Queijo and Mussarela):
      Pizza_queijo = True

    if(Queijo and Pizza_tresQueijos):
      Cheddar = True 

  else:
    print(f'(Pizza dois queijos) = Não\n')