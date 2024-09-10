import os
import uuid

def get_user_directory_path(instance, filename):
    _, ext = os.path.splitext(filename)

    # if hasattr(instance, 'empresa'):
    #     return f"user_{instance.empresa.user.id}/{uuid.uuid4()}{ext}"
    
    return f"user_{instance.user.id}/{uuid.uuid4()}{ext}"