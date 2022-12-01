import matplotlib.pyplot as plt


def gc_ratio_function(gc_input: str, step: int):
    def gc_count(gc: str) -> int:
        quantity = (gc.count('G') + gc.count('C')) / len(gc)
        return round(quantity * 100)

    distribution = []
    for section_start in range(0, len(gc_input) - step + 1, step):
        section_end = section_start + step
        section = gc_input[section_start:section_end]
        distribution.append(gc_count(section))

    plt.plot(distribution)
    plt.title('GC-content metric')
    plt.xlabel('Genome position')
    plt.ylabel('GC  (%)')
    plt.savefig('gc_ratio.png')
