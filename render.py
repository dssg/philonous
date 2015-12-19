import re

from beautifulsoup import BeautifulSoup

DEFAULT_MARKUP = '<ph-experiment></ph-experiment>'

class Renderer(object):
    def __init__(self):
        self.models = []
        self.markup_source = DEFAULT_MARKUP

    def register_model(self, clf, M_train, labels_train, M_test, labels_test, 
                       metadata):
        try: # see if clf has been fit yet
            clf.score()
        except TypeError:
            clf.fit(M_train, labels_train)
        model = {
                 'clf' : clf,
                 'M_train' : M_train,
                 'labels_train' : labels_train,
                 'M_test' : M_test,
                 'labels_test' : labels_test,
                 'metadata' : metadata
                 }
        self.models.append(model)

    def set_markup(self, source)
        """source is a file-like object or a string """
        self.markup_source = source

    def __experiment_to_env(self, env):
        # TODO stub
        # should copy env and populate with Experiment
        return env

    def __model_to_env(self, name, args, env):
        # TODO stub
        # should copy env and populate with correct model
        return env

    def __process_text(self, text, env):
        return re.sub(text, '\{\{.*\}\}', 'PHILONOUS_WAS_HERE')

    def __walk(self, in_soup, out_soup, env):
        # http://makble.com/parsing-and-traversing-dom-tree-with-beautifulsoup
        if in_soup.name is None: # text node (?)
            processed_string = self.__process_text(in_soup.string, env)
            out_soup.append(processed_string)
            return
        if in_soup.name == 'ph-experiment':
            new_tag = out_soup.new_tag('div')
            out_soup.append(new_tag)
            env = self.__experiment_to_env(env)
            out_soup = new_tag
        # TODO make sure we're not nesting ph-...-model tags
        elif in_soup.name in ('ph-model', 'ph-best-model'):
            new_tag = out_soup.new_tag('div')
            out_soup.append(new_tag)
            env = self.__model_to_env(in_soup.name, in_soup.attrs, env)
            out_soup = new_tag
        elif in_soup.name == 'ph-for-each-model':
            # TODO respect sorting
            for idx, model in enumerate(self.models):
                new_tag = out_soup.new_tag('div')
                # TODO here
                out_soup.append(new_tag)

        for child in in_soup.children:
            self.__walk(child)

    def run(self):
        in_soup = BeautifulSoup(self.markup_source)
        out_soup = BeautifulSoup()
        env = {}
        return self.__walk(in_soup, out_soup, env).prettify()


    
