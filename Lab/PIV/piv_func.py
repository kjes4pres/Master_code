from openpiv import tools, pyprocess, validation, filters, scaling

def perform_piv(key_a, window_size, overlap, search_area_size,
                scaling_factor, cropped_frames, timestamps,
                stepsize=1, threshold=1.4, max_iter=10, kernel_size=2):
    """
    Perform PIV analysis on a pair of frames and return the velocity field.
    This function utilizes the OpenPIV library to compute the velocity field between two frames, 
    applies validation and filtering, and scales the results to physical units.

    Parameters:
        key_a : int
            Index of the first frame in the pair.
        window_size : int
            Size of the interrogation window (in pixels).
        overlap : int
            Number of pixels by which the interrogation windows overlap.
        search_area_size : int
            Size of the search area for the second frame (in pixels).
        scaling_factor : float
            Factor to convert pixel displacements to physical units (pixel/m).
        cropped_frames : dict
            Dictionary containing the cropped frames, indexed by their original frame numbers.
        timestamps : list or array
            List of timestamps corresponding to each frame, indexed by their original frame numbers.
        stepsize : int, optional
            Number of frames to skip between the two frames used for PIV analysis (default is 1).
        threshold : float, optional
            Signal-to-noise ratio threshold for validating the velocity vectors (default is 1.4).
        max_iter : int, optional
            Maximum number of iterations for outlier replacement (default is 10).
        kernel_size : int, optional
            Size of the kernel for local mean outlier replacement (default is 2).

    Returns:
        x : 2D array
            x-coordinates of the velocity vectors (in physical units).
        y : 2D array
            y-coordinates of the velocity vectors (in physical units).
        u : 2D array
            x-components of the velocity vectors (in physical units).
        v : 2D array
            y-components of the velocity vectors (in physical units).

        The coordinate arrays (x, y) and velocity component arrays (u, v)
        are all scaled to physical units (e.g., meters and meters per second).

        The coordinate system is such that the origin (0,0)
        is at the top left corner of the image, with x increasing to the right and y increasing downwards.
    """
    
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
    # Get coordinates of center of interrogation windows
    # Origin is top left corner of the image, with x increasing to the right and y increasing downwards
    x, y = pyprocess.get_coordinates(image_size=frame_a.shape, search_area_size=search_area_size, overlap=overlap)
    
    # Mask out low signal-to-noise vectors
    u, v, mask = validation.sig2noise_val(u, v, sig2noise, threshold=threshold)

    # Replace values below the threshold with local mean values
    u, v = filters.replace_outliers(u, v, method='localmean', max_iter=max_iter, kernel_size=kernel_size)

    # Scale the vector field to physical units (m/s)
    x, y, u, v = scaling.uniform(x, y, u, v, scaling_factor=scaling_factor)

    return x, y, u, v