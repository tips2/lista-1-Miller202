Queijo = False
Pizza_queijo = False
Pizza_doisQueijos = False
Cheddar = False
Mussarela = False
Pizza_quatroQueijos = False

def facts():
  global Queijo
  Queijo = True

if __name__ == "__main__":
  facts()
  lim = range(0, 10)
  for i in lim:
    if(Queijo and Mussarela):
      Pizza_queijo = True

    if(Queijo and Pizza_quatroQueijos):
      Cheddar = True
    
    if(Pizza_doisQueijos):
      print(f'(Pizza dois queijos) = Sim\n')
      break

    if(Pizza_queijo and Cheddar):
      Pizza_doisQueijos = True

    if(Queijo):
      Mussarela = True
      Pizza_quatroQueijos = True

  else:
    print(f'(Pizza dois queijos) = Não\n')