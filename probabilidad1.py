def experiment_proba(n_experimentos):

  ## Contador
  contador = 0

  for i in range(n_experimentos):

    dado1 = np.random.randint(1,7)
    dado2 = np.random.randint(1,7)

    suma_dado = dado1 + dado2
    
    if (suma_dado > 7) or ((suma_dado % 2) == 0):
      contador+=1

  prop = contador / n_experimentos
