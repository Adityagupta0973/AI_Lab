# from tensorflow.keras.datasets import mnist
# import matplotlib.pyplot as plt
# import numpy as np

# # Load the MNIST dataset
# (X_train, y_train), (_, _) = mnist.load_data()

# # Print 4 images in a row
# plt.figure(figsize=(10, 5))
# for i in range(4):
#     plt.subplot(1, 4, i+1)
#     plt.imshow(X_train[i], cmap='gray')
#     plt.title(f"Label: {y_train[i]}")
#     plt.axis('off')
# plt.tight_layout()
# plt.show()

#PYTORCH
# import matplotlib.pyplot as plt
# import torch
# from torchvision import datasets, transforms

# # Define the transformation to convert images to PyTorch tensors
# transform = transforms.Compose([transforms.ToTensor()])

# # Load the MNIST dataset with the specified transformation
# mnist_pytorch = datasets.MNIST(root='./data', train=True, download=True, transform=transform)

# # Create a DataLoader to load the dataset in batches
# train_loader_pytorch = torch.utils.data.DataLoader(mnist_pytorch, batch_size=1, shuffle=False)

# # Create a figure to display the images
# plt.figure(figsize=(15, 3))

# # Print the first few images in a row
# for i, (image, label) in enumerate(train_loader_pytorch):
#     if i < 5:  # Print the first 5 samples
#         plt.subplot(1, 5, i + 1)
#         plt.imshow(image[0].squeeze(), cmap='gray')
#         plt.title(f"Label: {label.item()}")
#         plt.axis('off')
#     else:
#         break  # Exit the loop after printing 5 samples

# plt.tight_layout()
# plt.show()