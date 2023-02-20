from openpyxl import Workbook, load_workbook
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from tw_sentiment import TwSentiment

max_tweets_to_analyze = 50

class ExcelProcessor():
    def Open_excel(self, filenameInput):

        bookInput = load_workbook(filenameInput)

        sheet = bookInput.active
        
        return sheet
    
    def analyze_tweets(self, sheet):
        results = []
        
        count = 0

        analizer = TwSentiment()

        for row in sheet.values:
            #Pass the first row, as the first row is the header
            if count != 0:
                results.append(analizer.do_analize(row[1]))
            
            if count >= max_tweets_to_analyze:
                break
            
            count += 1
            
        return results
            
    def do_confution_matrix(self, sheet):
        y_true = []
        y_pred = []
        
        count = 0

        analizer = TwSentiment()

        for row in sheet.values:
            #Pass the first row, as the first row is the header
            if count != 0:
                sentiment = analizer.do_analize(row[1])
                print('Sentiment is: ' + sentiment)
                y_true.append(row[0])
                y_pred.append(sentiment)
            
            if count >= max_tweets_to_analyze:
                break
            
            count += 1
        
        cm = confusion_matrix(y_true, y_pred, labels=['NEGATIVE', 'NEUTRAL', 'POSITIVE'])
        cm_display = ConfusionMatrixDisplay(cm).plot()
        
        
        precision = precision_score(y_true, y_pred, average='macro')
        print('The precision of the modal is: %.2F' % precision)
        recall = recall_score(y_true, y_pred, average='macro')
        print('The recall of the modal is: is: %.2F' % recall)
        accuracy = accuracy_score(y_true, y_pred)
        print('The accuracy of the modal is: %.2F' % accuracy)
        
        plt.show()
        
            
if __name__ == "__main__":
    filenameInput = 'Tweets_with_polarity.xlsx'
    
    excel_pr = ExcelProcessor()
    
    excel_pr.analyze_tweets(excel_pr.Open_excel(filenameInput))
    
    excel_pr.do_confution_matrix(excel_pr.Open_excel(filenameInput))