import cowsay
import wikipedia


def random_article(namespace = None):
    return cowsay.cow( wikipedia.summary(wikipedia.random(), 10))
    # print(cowsay.get_output_string('trex','Hi, Bitches'))

random_article()