import datetime as dt

class day_usage:
    def __init__(self, date_str):
        self.dt = dt.datetime.strptime(date_str.replace(':\n', ' 2018' ), '%b %d %Y')
        self.usage=dict()

    def add_stuff(self, line):
        #	* 6 ml tannkrem
        stuff = line.split()
        self.usage[stuff[3]] = int(stuff[1])

    def day_of_week(self):
        return self.dt.weekday()

def calc_usage(log, stuff, pack_size=1, day_of_week=None):
    total_usage=0

    for du in log:
        if day_of_week is None or day_of_week == du.day_of_week():
            total_usage = total_usage + du.usage[stuff]
    
    return total_usage//pack_size

def main():
    log=list()
    for line in open("logg.txt").readlines():
        if line[0]!='\t':
            du = day_usage(line)
            log.append(du)
        else:
            du.add_stuff(line)
    
    print('tubes tandpasta:', calc_usage(log, 'tannkrem', 125))
    print('flessen shampoo:', calc_usage(log, 'sjampo', 300))
    print('rollen toiletpapier:', calc_usage(log, 'toalettpapir', 25))
    print('ml shampoo op zondag:', calc_usage(log, 'sjampo', day_of_week=6))
    print('m toiletpapier op woensdag:', calc_usage(log, 'toalettpapir', day_of_week=2))

    print('svar:', calc_usage(log, 'tannkrem', 125) * calc_usage(log, 'sjampo', 300) * calc_usage(log, 'toalettpapir', 25) * calc_usage(log, 'sjampo', day_of_week=6) * calc_usage(log, 'toalettpapir', day_of_week=2)) 

main()
