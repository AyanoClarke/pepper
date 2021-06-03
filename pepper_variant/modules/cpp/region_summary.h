//
// Created by Kishwar Shafin on 3/21/21.
//

#ifndef PEPPER_PRIVATE_REGION_SUMMARY_H
#define PEPPER_PRIVATE_REGION_SUMMARY_H

#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <utility>

namespace ImageOptionsRegion {
    static constexpr int MAX_COLOR_VALUE = 254;
    static constexpr int MISMATCH_COLOR_START = 128;
    static constexpr int REFERENCE_INDEX_START = 0;
    static constexpr int REFERENCE_INDEX_SIZE = 0;
    static constexpr int BASE_INDEX_START = 0;
    static constexpr int BASE_INDEX_SIZE = 22;
    vector<string> column_values{"ARFW:",
                                 "CRFW:",
                                 "GRFW:",
                                 "TRFW:",
                                 "ARRE:",
                                 "CRRE:",
                                 "GRRE:",
                                 "TRRE:",
                                 "AFRW:",
                                 "CFRW:",
                                 "GFRW:",
                                 "TFRW:",
                                 "IFRW:",
                                 "DFRW:",
                                 "*FRW:",
                                 "AREV:",
                                 "CREV:",
                                 "GREV:",
                                 "TREV:",
                                 "IREV:",
                                 "DREV:",
                                 "*REV:"};

    static constexpr bool GENERATE_INDELS = false;
};

struct type_truth_record{
    string contig;
    long long pos_start;
    long long pos_end;
    string ref;
    string alt;

    type_truth_record(string contig, long long pos, long long pos_end, string ref, string alt) {
        this->contig = std::move(contig);
        this->pos_start = pos;
        this->pos_end = pos_end;
        this->ref = std::move(ref);
        this->alt = std::move(alt);
    }
};


namespace VariantTypes {

    static constexpr int HOM_REF = 0;
    static constexpr int SNP = 1;
    static constexpr int INSERT = 2;
    static constexpr int DELETE = 3;
};

struct RegionalImageSummary {
    vector< vector< vector<uint8_t> > > chunked_image_matrix;
    vector< vector<int64_t> > chunked_positions;
    vector< vector<int32_t> > chunked_index;
    vector< vector<uint8_t> > chunked_labels;
    vector< vector<uint8_t> > chunked_type_labels;
    vector<int> chunked_ids;
};


struct CandidateImageSummary {
    string contig;
    int64_t position;
    int64_t region_start;
    int64_t region_stop;
    vector< vector<int> > image_matrix;
    uint8_t base_label;
    uint8_t type_label;
};

class RegionalSummaryGenerator {
    string contig;
    long long ref_start;
    long long ref_end;
    string reference_sequence;
    vector<char> labels_hp1;
    vector<char> labels_hp2;
    vector<int> variant_type_labels_hp1;
    vector<int> variant_type_labels_hp2;
    vector<char> ref_at_labels;
public:
    vector<uint16_t> labels;
    vector<uint16_t> labels_variant_type;
    vector<uint64_t> max_observed_insert;
    vector<uint64_t> positions;
    vector<uint32_t> index;
    vector<uint64_t> cumulative_observed_insert;
    uint64_t total_observered_insert_bases;

    RegionalSummaryGenerator(string contig, long long region_start, long long region_end, string reference_sequence);

    void generate_max_insert_observed(const type_read& read);

    void generate_max_insert_summary(vector <type_read> &reads);

    static int get_reference_feature_index(char base);

    void encode_reference_bases(vector< vector<int> >& image_matrix);

    void generate_labels(const vector<type_truth_record>& hap1_records, const vector<type_truth_record>& hap2_records);

    void populate_summary_matrix(vector< vector<int> >& image_matrix,
                                 int *coverage_vector,
                                 int *snp_count,
                                 int *insert_count,
                                 int *delete_count,
                                 type_read read);

    static int get_feature_index(char ref_base, char base, bool is_reverse);

    void debug_print_matrix(vector<vector<int> > image_matrix, bool train_mode);

    void debug_candidate_summary(CandidateImageSummary candidate, int small_chunk_size, bool train_mode);

    vector<CandidateImageSummary> generate_summary(vector <type_read> &reads,
                                                   double snp_freq_threshold,
                                                   double insert_freq_threshold,
                                                   double delete_freq_threshold,
                                                   double min_coverage_threshold,
                                                   long long candidate_region_start,
                                                   long long candidate_region_end,
                                                   int candidate_window_size,
                                                   int feature_size,
                                                   bool train_mode);
};

#endif //PEPPER_PRIVATE_REGION_SUMMARY_H
