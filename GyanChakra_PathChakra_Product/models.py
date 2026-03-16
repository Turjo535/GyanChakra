from django.db import models
from treebeard.mp_tree import MP_Node
from GyanChakra_Users.models import GyanChakraUserModel
# Create your models here.


class PathChakraModel(models.Model):
    book_name = models.CharField(max_length=100)
    author_name= models.CharField(max_length=100)
    description = models.TextField()
    total_pages= models.IntegerField()
    status = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='path_chakra_images/')

    def __str__(self):
        return self.book_name
    
class PathChakraBookChapterModels(MP_Node):
    path_chakra = models.ForeignKey(PathChakraModel, on_delete=models.CASCADE, related_name='chapters')
    chapter_name = models.CharField(max_length=100)
    node_order_by = ['chapter_name']
    def __str__(self):
        return self.chapter_name


class PathChakraUserAssignModel(models.Model):
    user = models.ForeignKey(GyanChakraUserModel, on_delete=models.CASCADE)
    path_chakra = models.ForeignKey(PathChakraModel, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.path_chakra.book_name}"