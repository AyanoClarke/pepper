class ImageSizeOptions(object):
    IMAGE_HEIGHT = 10
    IMAGE_CHANNEL_HEIGHT = 10
    IMAGE_CHANNELS = 1
    SEQ_LENGTH = 1000
    SEQ_OVERLAP = 50
    LABEL_LENGTH = SEQ_LENGTH

    TOTAL_LABELS = 5
    MIN_SEQUENCE_LENGTH = 1000
    MIN_IMAGE_OVERLAP = 100


class ReadFilterOptions(object):
    MIN_MAPQ = 10
    MIN_BASEQ = 0
    INCLUDE_SUPPLEMENTARY = False


class CandidateFinderOptions(object):
    ALLELE_FREQ_THRESHOLD = 0.05

    SNP_ALT_PROB_THRESHOLD = 0.1
    SNP_NON_REF_THRESHOLD = 0.1
    SNP_LAST_CHANCE_THRESHOLD = 0.1
    SNP_FREQ_THRESHOLD = 0.2

    IN_ALT_PROB_THRESHOLD = 0.1
    IN_NON_REF_THRESHOLD = 0.1
    IN_LAST_CHANCE_THRESHOLD = 0.1
    IN_FREQ_THRESHOLD = 0.2

    DEL_ALT_PROB_THRESHOLD = 0.1
    DEL_NON_REF_THRESHOLD = 0.1
    DEL_LAST_CHANCE_THRESHOLD = 0.1
    DEL_FREQ_THRESHOLD = 0.2

    SAFE_BASES = 20
    ALT_PROB_THRESHOLD = 0.1


class TrainOptions(object):
    # these two parameters are important, make sure you are sliding in a way that you cover the full sequence length
    # the training loop breaks when current_index + TRAIN_WINDOW > LAST_INDEX. You may lose information if you don't
    # slide correctly
    TRAIN_WINDOW = 100
    WINDOW_JUMP = 50
    GRU_LAYERS = 1
    HIDDEN_SIZE = 128


class AlingerOptions(object):
    # base and map quality
    ALIGNMENT_SAFE_BASES = 20
    MIN_MAP_QUALITY = 20

    MAX_READS_IN_REGION = 1500
    RANDOM_SEED = 2719747673

