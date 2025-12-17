import random
import time

# --- CONFIGURAÇÕES GLOBAIS ---
BASE_TICK = 10000
MAX_HAND_SIZE = 5
MAX_ETHER = 3  # Mana por turno (simplificado para 1v1)

class Card:
    def __init__(self, name, cost, effect_type, power, description):
        self.name = name
        self.cost = cost
        self.effect_type = effect_type # 'Attack', 'Defend', 'Buff', 'Special'
        self.power = power # Valor numérico base (dano, escudo, etc)
        self.description = description

    def __repr__(self):
        return f"[{self.cost}E] {self.name}"

class Musa:
    def __init__(self, name, role, hp, atk, def_, vel, passive_desc):
        self.name = name
        self.role = role
        self.max_hp = hp
        self.current_hp = hp
        self.atk = atk
        self.def_ = def_
        self.vel = vel
        self.passive_desc = passive_desc
        
        # Sistema de Turno
        self.action_value = int(BASE_TICK / self.vel)
        
        # Sistema de Recursos
        self.ether = 0
        self.ultimate_charge = 0 # 0 a 100
        self.shield = 0 # HP Temporário
        
        # Deck & Mão
        self.deck_list = [] # Template do deck
        self.draw_pile = [] # Pilha de compra
        self.hand = [] # Mão atual
        self.discard_pile = [] # Descarte
        
        self.is_alive = True
        self.status_effects = [] # Lista de dicionários {'name': 'Fuligem', 'duration': 2}

    def initialize_deck(self, cards):
        self.deck_list = cards
        self.shuffle_deck()

    def shuffle_deck(self):
        self.draw_pile = self.deck_list.copy()
        random.shuffle(self.draw_pile)
        self.discard_pile = []
        print(f"   (Deck de {self.name} reembaralhado!)")

    def draw_cards(self):
        needed = MAX_HAND_SIZE - len(self.hand)
        if needed <= 0:
            return
        
        print(f"   -> Comprando {needed} cartas...")
        for _ in range(needed):
            if not self.draw_pile:
                self.shuffle_deck()
            
            if self.draw_pile:
                card = self.draw_pile.pop()
                self.hand.append(card)

    def burn_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            card = self.hand.pop(card_index)
            self.discard_pile.append(card)
            self.ether += 1
            print(f"🔥 {self.name} QUEIMOU '{card.name}'! (+1 Éter)")
            return True
        return False

    def take_damage(self, amount):
        # Primeiro desconta do escudo
        remaining_dmg = amount
        if self.shield > 0:
            if self.shield >= remaining_dmg:
                self.shield -= remaining_dmg
                remaining_dmg = 0
                print(f"   (Escudo absorveu tudo!)")
            else:
                remaining_dmg -= self.shield
                self.shield = 0
                print(f"   (Escudo quebrado!)")
        
        if remaining_dmg > 0:
            # Mitigação física
            mitigation = 100 / (100 + (self.def_ * 0.5))
            final_dmg = int(remaining_dmg * mitigation)
            self.current_hp -= final_dmg
            print(f"   -> {self.name} recebeu {final_dmg} de dano! (HP: {self.current_hp}/{self.max_hp})")
            
            if self.current_hp <= 0:
                self.is_alive = False
                print(f"💀 {self.name} CAIU EM COMBATE!")

    def basic_attack(self, target):
        print(f"⚔️ {self.name} usa COMANDO BÁSICO em {target.name}!")
        dmg = int(self.atk * 0.8)
        target.take_damage(dmg)
        self.ultimate_charge = min(100, self.ultimate_charge + 15)
        print(f"   (+15 Carga Ult -> {self.ultimate_charge}%)")

    def cast_card(self, card, target):
        if self.ether < card.cost:
            print(f"❌ Sem Éter suficiente para {card.name}!")
            return False
        
        self.ether -= card.cost
        self.hand.remove(card)
        self.discard_pile.append(card)
        
        print(f"✨ {self.name} joga [{card.name}]!")
        
        # Lógica simplificada de efeitos para o MVP
        if card.effect_type == 'Attack':
            multiplier = card.power / 100.0
            dmg = int(self.atk * multiplier)
            # Bônus condicional simples (ex: Elysia bate mais em quem tem debuff)
            target.take_damage(dmg)
            
        elif card.effect_type == 'Defend':
            self.shield += card.power
            print(f"   -> Ganhou {card.power} de Escudo!")
            
        elif card.effect_type == 'DoT':
            print(f"   -> Aplicou PODRIDÃO em {target.name}!")
            
        return True

# --- MOTOR DE JOGO ---

def run_battle_simulation():
    # 1. Setup Musas (Baseado no GDD)
    
    # ELYSIA (Striker)
    elysia = Musa("Elysia", "Striker", hp=1800, atk=250, def_=80, vel=110, passive_desc="Dano+ por Debuff")
    deck_elysia = [
        Card("Corte de Cinzas", 1, 'Attack', 120, "Dano + Fuligem"),
        Card("Corte de Cinzas", 1, 'Attack', 120, "Dano + Fuligem"),
        Card("Corte de Cinzas", 1, 'Attack', 120, "Dano + Fuligem"), # 3 cópias
        Card("Vento Abrasador", 1, 'Attack', 80, "AoE"),
        Card("Pilar de Fumaça", 2, 'Attack', 100, "Cega o alvo"),
        Card("Desmoronar", 2, 'Attack', 150, "Crítico em Fuligem"),
        Card("Fênix Cinzenta", 3, 'Attack', 200, "Dano + Cura")
    ]
    elysia.initialize_deck(deck_elysia)
    
    # VEX (Tank/Controller)
    vex = Musa("Vex", "Controller", hp=2400, atk=180, def_=140, vel=95, passive_desc="Cura com DoT")
    deck_vex = [
        Card("Esporos Nocivos", 1, 'DoT', 50, "Aplica DoT"),
        Card("Esporos Nocivos", 1, 'DoT', 50, "Aplica DoT"),
        Card("Barreira de Raízes", 1, 'Defend', 300, "Escudo"),
        Card("Barreira de Raízes", 1, 'Defend', 300, "Escudo"),
        Card("Parasita", 2, 'Special', 0, "Deixa Vulnerável"),
        Card("Decomposição", 2, 'Attack', 100, "Estoura DoTs"),
        Card("Transplante", 3, 'Special', 0, "Sacrifica HP por Ult")
    ]
    vex.initialize_deck(deck_vex)
    
    participants = [elysia, vex]
    turn_limit = 10
    current_turn = 0
    
    print("\n⚔️ === INÍCIO DO COMBATE MVP === ⚔️")
    print(f"{elysia.name} VS {vex.name}\n")
    
    while current_turn < turn_limit and elysia.is_alive and vex.is_alive:
        # Sort by Action Value (Menor valor age primeiro)
        participants.sort(key=lambda p: p.action_value)
        active_char = participants[0]
        enemy = participants[1] # Em 1v1 é sempre o outro
        
        # Avançar o tempo
        passed_time = active_char.action_value
        print(f"\n⏱️ T-{current_turn+1} | Avançando {passed_time} ticks...")
        for p in participants:
            p.action_value -= passed_time
            # Tick de DoT ou Regen aconteceria aqui
            
        print(f"🔷 TURNO DE {active_char.name} (HP: {active_char.current_hp} | Ult: {active_char.ultimate_charge}%)")
        
        # 1. Fase de Recarga
        active_char.ether = MAX_ETHER
        active_char.draw_cards()
        print(f"   Mão: {active_char.hand}")
        
        # 2. IA Lógica (Simulação de Jogador)
        # Tenta usar carta cara -> Se não der, queima carta fraca -> Tenta de novo
        # Se nada der certo -> Ataque Básico
        
        has_acted = False
        
        # Tenta jogar a carta mais forte da mão (Custo maior)
        sorted_hand = sorted(active_char.hand, key=lambda c: c.cost, reverse=True)
        
        if sorted_hand:
            chosen_card = sorted_hand[0]
            
            # Se não tem mana, tenta queimar a carta mais barata para pagar a cara
            if active_char.ether < chosen_card.cost:
                cheapest = sorted_hand[-1]
                if cheapest != chosen_card:
                    active_char.burn_card(active_char.hand.index(cheapest))
            
            # Tenta jogar
            if active_char.ether >= chosen_card.cost:
                active_char.cast_card(chosen_card, enemy)
                has_acted = True
            else:
                print("   (Preferiu guardar mana...)")
                
        if not has_acted:
            active_char.basic_attack(enemy)
            
        # 3. Reset Delay
        delay = int(BASE_TICK / active_char.vel)
        active_char.action_value = delay
        current_turn += 1
        time.sleep(1.5)

    print("\n🏆 FIM DA SIMULAÇÃO")
    if elysia.is_alive: print(f"Vencedora: {elysia.name}")
    elif vex.is_alive: print(f"Vencedora: {vex.name}")

if __name__ == "__main__":
    run_battle_simulation()