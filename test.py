
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

ids= ["allswell", "asyoulikeit", "comedy_errors", "cymbeline", "lll", "measure", "merry_wives", "merchant", "midsummer", "much_ado", "pericles", "taming_shrew", "tempest", "troilus_cressida", "twelfth_night", "two_gentlemen", "winters_tale", "1henryiv", "2henryiv", "henryv", "1henryvi", "2henryvi", "3henryvi", "henryviii", "john", "richardii", "richardiii", "cleopatra", "coriolanus", "hamlet", "julius_caesar", "lear", "macbeth", "othello", "romeo_juliet", "timon", "titus"]
titles = ["All's Well That Ends Well" , "As You Like It", "The Comedy of Errors", "Cymbeline", "Love's Labours Lost", "Measure for Measure", "The Merry Wives of Windsor", "The Merchant of Venice", "A Midsummer Night's Dream", "Much Ado About Nothing", "Pericles, Prince of Tyre", "Taming of the Shrew", "The Tempest", "Troilus and Cressida", "Twelfth Night", "Two Gentlemen of Verona", "Winter's Tale", "Henry IV, part 1", "Henry IV, part 2", "Henry V", "Henry VI, part 1", "Henry VI, part 2", "Henry VI, part 3", "Henry VIII", "King John", "Richard II", "Richard III", "Antony and Cleopatra", "Coriolanus", "Hamlet", "Julius Caesar", "King Lear", "Macbeth", "Othello", "Romeo and Juliet", "Timon of Athens", "Titus Andronicus"]


index=0
table = []
for play_id in ids:
	webpage = urlopen("http://shakespeare.mit.edu/" + play_id +"/full.html")
	soup = BeautifulSoup( webpage.read(), features="lxml")
	text = soup.get_text()
	table.append([play_id, titles[index], text[100:]])
	index += 1



with open('full_texts.csv', mode='w') as full_texts:
	text_writer = csv.writer(full_texts, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	text_writer.writerows(table)
