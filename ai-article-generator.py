import openai

OPEN_AI_ENGINE = 'text-davinci-002'
OPEN_AI_API_KEY = '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'

openai.api_key = OPEN_AI_API_KEY

def generate_title(keywords):
    result = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt="write only one blog post title about {}".format(keywords),
        temperature=0.7,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return result['choices'][0]['text'].replace('\n\n', '\n')

def generate_outline(title):
    result = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt="generate a professional blog outline for a post about {}".format(
            title),
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return result['choices'][0]['text'].replace('\n\n', '\n')

def generate_section(topic):
    result = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt="generate two paragraphs of minimum 800 words on topic {}".format(
            topic),
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return result['choices'][0]['text'].replace('\n\n', '\n')

def generate_article(keywords):
    article = ""
    title = generate_title(keywords)

    print(
        f"\nWAIT A FEW MINUTES\SECONDS GENERATING YOUR ARTICLE ON TOPIC : {title.upper()} \n")

    section_topics = [x for x in generate_outline(title).split('\n') if x != '']
    for section_topic in section_topics:
        article += "\n\n" + section_topic.upper() + "\n"
        article += generate_section(section_topic)

    print("WORD COUNT : " + str(len(article.split())))

    return article + "\n"

if __name__ == "__main__":
    keywords = input("ENTER SOME KEYWORDS FOR GENERATING ARTICLE : ")

    article = generate_article(keywords)
    print(article)
