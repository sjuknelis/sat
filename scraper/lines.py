from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
import json

def create_browser():
    service = Service(executable_path='./chromedriver')

    options = Options()
    options.add_argument("--headless")
    
    browser = webdriver.Chrome(service=service, options=options)
    return browser

def get_paragraph_lines(browser, paragraph):
    quoted_paragraph = quote(paragraph, safe='~()*!.\'')
    browser.get(f"http://localhost:8000/?{quoted_paragraph}")

    element = browser.find_element("id", "lines")
    text_content = element.text

    return json.loads(text_content)

def get_passage_lines(passage):
    browser = create_browser()
    lines = []

    for paragraph in passage.split("\n"):
        lines += get_paragraph_lines(browser, paragraph)
    
    browser.quit()
    return lines

if __name__ == "__main__":
    passage = "The “wisdom of crowds” has become a mantra of the Internet age. Need to choose a new vacuum cleaner? Check out the reviews on online merchant Amazon. But a new study suggests that such online scores don’t always reveal the best choice. A massive controlled experiment of Web users finds that such ratings are highly susceptible to irrational “herd behavior”—and that the herd can be manipulated.\nSometimes the crowd really is wiser than you. The classic examples are guessing the weight of a bull or the number of gumballs in a jar. Your guess is probably going to be far from the mark, whereas the average of many people’s choices is remarkably close to the true number.\nBut what happens when the goal is to judge something less tangible, such as the quality or worth of a product? According to one theory, the wisdom of the crowd still holds—measuring the aggregate of people’s opinions produces a stable, reliable value. Skeptics, however, argue that people’s opinions are easily swayed by those of others. So nudging a crowd early on by presenting contrary opinions—for example, exposing them to some very good or very bad attitudes—will steer the crowd in a different direction. To test which hypothesis is true, you would need to manipulate huge numbers of people, exposing them to false information and determining how it affects their opinions.\nA team led by Sinan Aral, a network scientist at the Massachusetts Institute of Technology in Cambridge, did exactly that. Aral has been secretly working with a popular website that aggregates news stories. The website allows users to make comments about news stories and vote each other’s comments up or down. The vote tallies are visible as a number next to each comment, and the position of the comments is chronological. (Stories on the site get an average of about ten comments and about three votes per comment.) It’s a follow-up to his experiment using people’s ratings of movies to measure how much individual people influence each other online (answer: a lot). This time, he wanted to know how much the crowd influences the individual, and whether it can be controlled from outside.\nFor five months, every comment submitted by a user randomly received an “up” vote (positive); a “down” vote (negative); or as a control, no vote at all. The team then observed how users rated those comments. The users generated more than 100,000 comments that were viewed more than 10 million times and rated more than 300,000 times by other users.\nAt least when it comes to comments on news sites, the crowd is more herdlike than wise. Comments that received fake positive votes from the researchers were 32% more likely to receive more positive votes compared with a control, the team reports. And those comments were no more likely than the control to be down-voted by the next viewer to see them. By the end of the study, positively manipulated comments got an overall boost of about 25%. However, the same did not hold true for negative manipulation. The ratings of comments that got a fake down vote were usually negated by an up vote by the next user to see them.\n“Our experiment does not reveal the psychology behind people’s decisions,” Aral says, “but an intuitive explanation is that people are more skeptical of negative social influence. They’re more willing to go along with positive opinions from other people.”\nDuncan Watts, a network scientist at Microsoft Research in New York City, agrees with that conclusion. “[But] one question is whether the positive [herding] bias is specific to this site” or true in general, Watts says. He points out that the category of the news items in the experiment had a strong effect on how much people could be manipulated. “I would have thought that ‘business’ is pretty similar to ‘economics,’ yet they find a much stronger effect (almost 50% stronger) for the former than the latter. What explains this difference? If we’re going to apply these findings in the real world, we’ll need to know the answers.”\nWill companies be able to boost their products by manipulating online ratings on a massive scale? “That is easier said than done,” Watts says. If people detect—or learn—that comments on a website are being manipulated, the herd may spook and leave entirely."
    print(get_passage_lines(passage))

