from .models import Movie
from neomodel import db


MODELS = {
    'Movie': Movie,
}

def filter_nodes(node_type):
    node_set = node_type.nodes

    return node_set

def fetch_nodes(fetch_info):
    node_type = fetch_info['node_type']
    page = int(fetch_info['page'])

    node_set = filter_nodes(MODELS[node_type])

    page_limit = 200

    node_set = node_set[(page-1)*page_limit:((page)*page_limit)]

    return [node.serialize for node in node_set]