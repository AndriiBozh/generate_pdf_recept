import pandas
from reportlab.pdfgen.canvas import Canvas

df = pandas.read_csv("Articles.csv")

class Article:
    def __init__(self, id):
        self.id = id

        matched_rows = df.loc[df['id'] == self.id, ['name', 'price', 'in stock']] # select multiple columns

        if not matched_rows.empty:
            self.name = matched_rows['name'].values[0]
            self.price = matched_rows['price'].values[0]
            self.in_stock = matched_rows['in stock'].values[0]
        else:
            self.name = 'Article not found'
            self.price = None
            self.in_stock = None


    def decrement_items_quantity(self):
        if self.in_stock > 0:
            self.in_stock -= 1
            df.loc[df['id'] == self.id, 'in stock'] = self.in_stock
            df.to_csv('Articles.csv', index=False)


    def generate_pdf(self):
        if " " in self.name:
            self.name = self.name.replace(" ", "_")
        c = Canvas(f'{self.name}.pdf')
        text_obj = c.beginText()
        text_obj.setTextOrigin(0, 800)
        text_obj.setFont('Helvetica', 14)
        text_obj.textLine(f'Name: {self.name}')
        text_obj.textLine(f'Price: {self.price}')
        text_obj.textLine(f'In stock: {self.in_stock}')


        c.drawText(text_obj)
        c.save()


article_id = int(input('Please enter id of an article: '))

article_1 = Article(article_id)
article_1.decrement_items_quantity()
article_1.generate_pdf()


