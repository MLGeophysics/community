# Generative Adversarial Network

A Generative Adversarial Network (GAN) consists of two neural networks, a generator and a discriminator, that are trained simultaneously. The generator takes a randomly-drawn latent vector and produces an image (here, a well log). The discriminator takes an image (well log), and classifies it as belonging to the training set, or as coming from the generator. As the generator gets better at producing images, the discriminator must get better at telling generated images from training images. The goal is to train the generator to produce images that are as similar to the training set as possible.

Here, we trained a GAN on RILD logs from the Kansas Geological survey. This is a bit different than the usual application of GANs since the training set consists of 1D data, not 2D pictures.

{notebook:docs/projects/well_log_generator/GAN_KGS_RILD_60ft.ipynb}
