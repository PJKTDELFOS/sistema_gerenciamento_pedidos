class AppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'procesos':
            return 'processos_db'
        elif model._meta.app_label == 'contracts':
            return 'contratos_db'
        elif model._meta.app_label == 'documents':
            return 'documentos_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'procesos':
            return 'processos_db'
        elif model._meta.app_label == 'contracts':
            return 'contratos_db'
        elif model._meta.app_label == 'documents':
            return 'documentos_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'procesos':
            return db == 'processos_db'
        elif app_label == 'contracts':
            return db == 'contratos_db'
        elif app_label == 'documents':
            return db == 'documentos_db'
        return db == 'default'