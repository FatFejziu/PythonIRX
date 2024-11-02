import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Lesson13\example.csv")

filtered_df=df[df["people">= 18]]

filtered_df=filtered_df.sort_values(by="Average age",ascending=False)

print(filtered_df)

plt.figure(figisize=(14,8))

bars=plt.bar(filtered_df["Name"],filtered_df["Age"],filtered_df["City"],color="skyblue")

plt.title("Average age from people (Age >= 18)",fontsize=16)

plt.xlabel("Name",fontsize=14)
plt.ylabel("Age",fontsize=14)

plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)

plt.grid(axis="y",linestyle="--", alpha=0.8)
plt.bar_label(bars,fontsize=10, color="black")

plt.tight_layout()
plt.show()