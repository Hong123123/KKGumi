from conf import RESOURCE_FOLDER


def upload_resource(file, user, path):
    pass


def create_resource(filename, uid, filepath):
    from models.resource import Resource
    from models import db
    from os import path
    from os import makedirs
    secure_filename(filename)
    if not path.exists(RESOURCE_FOLDER + filepath):
        makedirs(RESOURCE_FOLDER + filepath)
    new_file = open(path.join(RESOURCE_FOLDER + filepath, filename), "w")
    new_resource = Resource(resource_name=filename, resource_path=filepath, uploader_uid=uid)
    db.session.add(new_resource)
    db.session.commit()
    return new_resource.rid


def update_resource(res, content, uid):
    from os import path
    # check user privilege
    if res.uploader_uid != uid:
        return False
    file = open(path.join(RESOURCE_FOLDER + res.resource_path, res.resource_name), "w")
    file.write(content)
    file.close()
    return True


def delete_resource(res, uid):
    pass


def secure_filename(filename):
    from re import search
    assert search("^\.", filename) is None
    assert search("/", filename) is None


def retrieve_info(filepath):
    from conf import RESOURCE_FOLDER
    from models.resource import Resource
    from os import path
    abspath = path.abspath(RESOURCE_FOLDER + filepath)
    basename = path.basename(abspath)
    dirname = path.dirname(abspath)
    resource_path = path.dirname(filepath)
    res = Resource.query.filter_by(resource_path=resource_path, resource_name=basename)
    accessibility = True
    if res.count() != 0 and res[0].public_access is False:
        accessibility = False
    return dirname, basename, accessibility