def validate_fastq(file):
    if not file.endswith('.fastq'):
        raise ValueError('Invalid file type')
echo def validate_sequence_length(file):
    if len(file) < 100:
        raise ValueError('Sequence too short')
