import pandas as pd
from sodapy import Socrata
import matplotlib.pyplot as plt



client = Socrata("www.datos.gov.co", None)
results = client.get("gt2j-8ykr")
results_df = pd.DataFrame.from_records(results)


#fig1=results_df.groupby('departamento')['id_de_caso'].count().plot(kind='barh')
fig2=results_df.groupby('sexo')['id_de_caso'].count().plot(kind='pie', autopct="%0.1f %%",legend='Comportamiento sexo/numero de casos')
#fig3=results_df.groupby('edad')['id_de_caso'].count().plot(kind='bar',legend='Comportamiento edad/numero de casos')
plt.show()

