import pandas as pd

class RescuePet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

    def process_adoption(self):
        self.is_adopted = True


df1 = pd.read_csv("shelter_A.csv")
df2 = pd.read_csv("shelter_B.csv")

df = pd.concat([df1, df2], ignore_index=True)

df = df.dropna()

dogs_df = df[df["Animal_Type"] == "Dog"]

dog_row = dogs_df.iloc[0]

pet = RescuePet(dog_row["Pet_Name"], dog_row["Animal_Type"], dog_row["Age_Years"])

pet.process_adoption()

adoption_data = pd.DataFrame([{
    "Pet_Name": pet.name,
    "Animal_Type": pet.species,
    "Age_Years": pet.age,
    "is_adopted": pet.is_adopted
}])

adoption_data.to_csv("successful_adoptions.csv", mode='a', header=not pd.io.common.file_exists("successful_adoptions.csv"), index=False)

print("Adoption saved successfully!")