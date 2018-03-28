

class Substitute(object):
    def __init__(self, compound, modifier_alts, head_alts, combined_alts):
        self.compound = compound
        self.modifier_alts = modifier_alts
        self.head_alts = head_alts
        self.combined_alts = combined_alts

    def print_all(self):
        print '\n================================='
        print self.compound
        print self.modifier_alts, ' SIZE: ', len(self.modifier_alts)
        print self.head_alts, ' SIZE: ', len(self.head_alts)
        print self.combined_alts, ' SIZE: ', len(self.combined_alts)
        print '=================================\n'
