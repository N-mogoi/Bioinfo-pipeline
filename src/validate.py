def validate_fastq(file):
    if not file.endswith('.fastq'):
        raise ValueError('Invalid file type')
