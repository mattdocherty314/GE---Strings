# --- IMPORT ---

import random



# --- VARIABLE INITIALISE ---

chromosomes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',
               '1', '2', '3', '4', '5', '6', '7', '8', '9',
               '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               '`', '~', '!', '@', '#', '$', '%', '^', '&',
               '(', ')', '-', '_', '=', '+', '[', '{', ']',
               '}', ';', "'", ',', '.']
#\/:*?"<>|
species = []
fitnessSpecies = []

generation = 0



# --- ADDITIONAL FUNCTIONS ---

# - customSort -
def customSort(fitnessSpecies):
    arraySorted = False
    while (not arraySorted):
        swapped = False
        for a in range(len(fitnessSpecies)-2):
            if (float(fitnessSpecies[a][0:4])) > float(fitnessSpecies[a+1][0:4]):
                fitnessTEMP = fitnessSpecies[a]
                fitnessSpecies[a] = fitnessSpecies[a+1]
                fitnessSpecies[a+1] = fitnessTEMP
                swapped = True
        if (not swapped):
            arraySorted = True



# --- RUN PROGRAM ---

# - Input & Output -
wantGene = input("Enter the wanted gene: ")
mutateChance = int(input("Enter the mutatation chance (1/x): "))
speciesNumber = int(input("Enter the number of species per generation: "))
generationNumber = int(input("Enter the number of generations: "))

s = open(("GE-Strings ('"+str(wantGene)+"'-"+str(generationNumber)+" generations-"
         +str(speciesNumber)+" species-"+str(mutateChance/100)+"% mutateChance).txt"), 'w')
s.write("wantGene = '"+str(wantGene)+"'\n")
s.write(str(generationNumber)+" generations\n")
s.write(str(speciesNumber)+" species\n")
s.write(str(mutateChance/100)+"% mutateChance)\n")

# - Predict Time To Take -
seconds = (generationNumber * speciesNumber * (len(wantGene)/20))/100
print("Estimated Time to Complete: "+str(seconds)+" seconds,")
minutes = seconds/60
print("OR "+str(minutes)+ " minutes,")
hours = minutes/60
print("OR "+str(hours)+" hours.")

# - Generate Random Species -
for a in range(speciesNumber):
    gene = ""
    for b in range(random.randint(2, (len(wantGene)+len(wantGene)-2))):
        gene += chromosomes[random.randint(0, len(chromosomes))-1]
    species.append(gene)

while generation < generationNumber:
    print("Generation: " + str(generation))
    s.write("\n----------------------------------------------------------------------------------------------------")
    s.write("\nGeneration: " + str(generation))
    s.write("\n")
    s.write("Species: \n(new)\n")
    s.write(str(species))

    # - Evaluate Fitness -
    for d in range(len(species)):
        fitness = 0
        for e in range(len(wantGene)):
            if (e < len(species[d])):
                if (species[d][e] == wantGene[e]):
                    fitness += 10
                else:
                    fitness -= 0.5
        fitness -= ((abs(len(species[d])-len(wantGene)))*0.2)
        fitnessSpecies.append(str(fitness)+":"+str(d))

    # - Format \fitnessSpecies -
    for g in range(len(fitnessSpecies)):
        fitnessTEMP, labelTEMP = fitnessSpecies[g].split(":")
        fitness2TEMP = list(fitnessTEMP)
        label2TEMP = list(labelTEMP)
        fitness3TEMP = []
        if (fitness2TEMP[0] != "-"):
            fitness2TEMP.reverse()
            fitness2TEMP.append("+")
            fitness2TEMP.reverse()
        for h in range(len(str(len(species)))-(len(label2TEMP))):
            label2TEMP.reverse()
            label2TEMP.append("0")
            label2TEMP.reverse()
        for g in range((len(str(len(wantGene))))-(len(fitness2TEMP))):
             fitness2TEMP = list(fitness3TEMP)
             fitness3TEMP = fitness2TEMP[0]
             fitness3TEMP.append("0")
             fitness3TEMP = "".join(fitness3TEMP)
             fitness2TEMP.reverse()
             fitness2TEMP.append(fitness3TEMP)
        
        fitnessTEMP = "".join(fitness2TEMP)
        
        fitnessTEMP = fitnessTEMP[0:(len(str(len(wantGene)))+4)]
        labelTEMP = "".join(label2TEMP)
        fitnessSpecies[g] = fitnessTEMP+":"+labelTEMP
        
    s.write("\n")
    s.write("Fitness: \n")
    s.write(str(fitnessSpecies))

    # - Remove Lower Half -
    customSort(fitnessSpecies)
    for j in range(int(len(species)/2)):
        species.pop(int(fitnessSpecies[j][(len(str(len(wantGene)))+5):((len(str(len(wantGene)))+4)+(len(str(len(species)))))]))
    fitnessSpecies = []

    # - Breed First and Second -
    for m in range(0, int(len(species)), 2):
        if (len(species[m]) >= len(species[m+1])):
            random_splicePosition = random.randint(1, (len(species[m+1])-1))
        else:
            random_splicePosition = random.randint(1, (len(species[m])-1))
        A1_geneSpliceTEMP = species[m][:random_splicePosition]
        B1_geneSpliceTEMP = species[m+1][:random_splicePosition]
        A2_geneSpliceTEMP = species[m][random_splicePosition:]
        B2_geneSpliceTEMP = species[m+1][random_splicePosition:]
        species.append(A1_geneSpliceTEMP+B2_geneSpliceTEMP)
        species.append(A2_geneSpliceTEMP+B1_geneSpliceTEMP)

    # - Add Mutations

    for p in range(len(species)):
        check_mutateChance = random.randint(1, mutateChance)
        if (check_mutateChance == 1):
            mutateType = random.randint(1,8)
            speciesTEMP = list(species[p])
            if ((mutateType == 1) and (len(speciesTEMP) > 2)):
                speciesTEMP.pop(random.randint(0, len(speciesTEMP)-1))
            elif ((mutateType == 2) and (len(wantGene)+len(wantGene)-2)):
                speciesTEMP.append(chromosomes[random.randint(0, len(chromosomes)-1)])
            else:
                speciesTEMP[random.randint(1, (len(speciesTEMP)))-1] = chromosomes[random.randint(1, (len(chromosomes)))-1]
            species[p] = "".join(speciesTEMP)
    
    # - Additional Instructions - 
    generation += 1
s.close()
if (wantGene in species):
    print("It has been successful!")


