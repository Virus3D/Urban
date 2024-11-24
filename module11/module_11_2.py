def introspection_info(obj):
    import inspect
    
    # Получаем тип объекта
    obj_type = type(obj).__name__
    
    # Получаем атрибуты объекта
    attributes = dir(obj)
    
    # Получаем методы объекта (только методы, не включая атрибуты)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # Получаем модуль, к которому принадлежит объект
    obj_module = None
    if hasattr(obj, '__module__'):
        obj_module = obj.__module__

    # Собираем информацию о интересных свойствах
    interesting_properties = {}

    if isinstance(obj, type):  # Если obj является классом
        interesting_properties['base_classes'] = obj.__bases__  # Суперклассы
        interesting_properties['is_abstract'] = inspect.isabstract(obj)  # Является ли класс абстрактным

    if hasattr(obj, '__dict__'):  # Если у объекта есть __dict__
        interesting_properties['class_attributes'] = obj.__dict__.keys()  # Атрибуты класса
    
    if inspect.isfunction(obj):  # Если объект - это функция
        interesting_properties['is_builtin'] = obj.__module__ == 'builtins'  # Встроенная ли функция

    if hasattr(obj, '__call__'):  # Если объект вызываемый
        interesting_properties['is_callable'] = True
    else:
        interesting_properties['is_callable'] = False

    # Собираем результаты в словарь
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'interesting_properties': interesting_properties,
    }

    # Возвращаем информацию
    return info


number_info = introspection_info(42)
print(number_info)