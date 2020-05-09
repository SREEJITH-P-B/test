import pandas as pd
df=pd.read_csv('data1.csv')
df.to_html('ttt.html')
import pdfkit
pdfkit.from_file('ttt.html', 'out.pdf')

