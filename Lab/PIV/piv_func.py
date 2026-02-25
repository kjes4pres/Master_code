from openpiv import tools, pyprocess, validation, filters, scaling

def perform_piv(key_a, window_size, overlap, search_area_size,
                scaling_factor, cropped_frames, timestamps,
                stepsize=1, threshold=1.4, max_iter=10, kernel_size=2):
    
    frame_a = cropped_frames[key_a]
    frame_b = cropped_frames[key_a + stepsize]
    
    idx_a = key_a - 1250
    idx_b = idx_a + stepsize

    time_a = timestamps[idx_a]
    time_b = timestamps[idx_b]

    dt = time_b - time_a

    # Perform PIV analysis
    u, v, sig2noise = pyprocess.extended_search_area_piv(
    frame_a, frame_b, 
    window_size=window_size, 
    overlap=overlap, 
    dt=dt*stepsize, 
    search_area_size=search_area_size
    )
    # Get coordinates of the vector field
    x, y = pyprocess.get_coordinates(image_size=frame_a.shape, search_area_size=search_area_size, overlap=overlap)
    
    # Validate the vector field using the signal-to-noise ratio
    u, v, mask = validation.sig2noise_val(u, v, sig2noise, threshold=threshold)

    # Replace values below the threshold with local mean values
    u, v = filters.replace_outliers(u, v, method='localmean', max_iter=max_iter, kernel_size=kernel_size)

    # Scale the vector field to physical units (e.g., m/s)
    x, y, u, v = scaling.uniform(x, y, u, v, scaling_factor=scaling_factor)

    return x, y, u, v