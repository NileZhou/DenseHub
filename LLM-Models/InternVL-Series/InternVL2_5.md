# Dataflow

## Image processing
max_num: 12  ?
1. load image then convert to RGB
2. transform image to 448*448   
ps: In computer vision area, 224 * 224 is the most common size to deal.   
3. to tensor then normalize using imagenet mean and std  
ps:   
IMAGENET_MEAN = (0.485, 0.456, 0.406)  
IMAGENET_STD = (0.229, 0.224, 0.225)  
```python
import torchvision.transforms as T
from torchvision.transforms.functional import InterpolationMode

def build_transform(input_size):
    transform = T.Compose([
        T.Lambda(lambda img: img.convert('RGB') if img.mode != 'RGB' else img),
        T.Resize((input_size, input_size), interpolation=InterpolationMode.BICUBIC),
        T.ToTensor(),
        T.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD)
    ])
    return transform
```



ps: imagenet
-  
