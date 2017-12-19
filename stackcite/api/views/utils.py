def config_views(config, endpoint):
    children = [n for n in endpoint if n[0] is not '_']
    for name, cfg in endpoint.items():
        model = cfg.get('_model')
        resource = cfg.get('_resource')
        views = resource.get('_views')
        attr_conf = views.get('_attr')
        views = views.get('_cls')
        resource = resource.get('_cls')
