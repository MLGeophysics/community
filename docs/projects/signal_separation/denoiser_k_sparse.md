# Sparse signal denoising   

Sometimes we know a signal of interest may be sparsely represented in a particular domain, for example band limited signals in the Fourier domain.  Observations of these signals probably contain noise that is difficult to remove.  We can train a neural network to separate signal from noise by teaching it the character of k-sparse signals during training.  

{notebook:docs/projects/signal_separation/denoiser_k_sparse.ipynb}

