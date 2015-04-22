__author__ = 'Antoine'

class ChartBoard():

    def __init__(self, champ_list):
        self.champ_list = champ_list


    def process_means(self, champion_list):

        mana_count = 0
        energy_count = 0

        tot_health = 0.0
        tot_ad = 0.0
        tot_health_reg = 0.0
        tot_mana = 0.0
        tot_mana_reg = 0.0
        tot_att_speed = 0.0
        tot_mov_speed = 0.0
        tot_armor = 0.0
        tot_mag_res = 0.0
        tot_range = 0.0
        tot_energy = 0.0
        tot_energy_reg = 0.0

        for champion in champion_list:

            tot_health += champion.health
            tot_ad += champion.ad
            tot_health_reg += champion.health_reg
            tot_att_speed += champion.att_speed
            tot_mov_speed += champion.mov_speed
            tot_armor += champion.armor
            tot_mag_res += champion.mag_res
            tot_range += champion.range
            if champion.mana is not None:
                mana_count += 1
                tot_mana +=  champion.mana
                tot_mana_reg += champion.mana_reg
            if champion.energy is not None:
                energy_count += 1
                tot_energy += champion.energy
                tot_energy_reg += champion.energy_reg

        nb_champ = len(champion_list)

        means = dict()
        means["health"] = tot_health / nb_champ
        means["health_reg"] = tot_health_reg / nb_champ
        means["ad"] = tot_ad / nb_champ
        means["att_speed"] = tot_att_speed / nb_champ
        means["mov_speed"] = tot_mov_speed / nb_champ
        means["armor"] = tot_armor / nb_champ
        means["mag_res"] = tot_mag_res / nb_champ
        means["range"] = tot_range / nb_champ
        means["mana"] = tot_mana / mana_count
        means["mana_reg"] = tot_mana_reg / mana_count
        means["energy"] = tot_energy / energy_count
        means["energy_reg"] = tot_energy_reg / energy_count

        return means


