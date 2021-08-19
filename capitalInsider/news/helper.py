def get_dates(lst):
    archive = []
    for date in lst:
        if date not in archive:
            archive.append(date)

    return archive
    