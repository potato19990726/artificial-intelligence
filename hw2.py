def AND(*args):
    return all(args)

def OR(*args):
    return any(args)

def NOT(a):
    return not a

class Rule:
    def __init__(self, condition, action, priority=0):
        self.condition = condition
        self.action = action
        self.priority = priority

    def __str__(self):
        return f"Rule(condition={self.condition}, action={self.action}, priority={self.priority})"

    def evaluate(self, facts):
        return self.condition.evaluate(facts)

class Condition:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __str__(self):
        return f"Condition(func={self.func.__name__}, args={self.args})"

    def evaluate(self, facts):
        return self.func(*[arg.evaluate(facts) if isinstance(arg, Condition) else facts.get(arg, arg) for arg in self.args])

class Fact:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Fact(name={self.name}, value={self.value})"

class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = {}  # Changed to dictionary for easier lookup

    def add_rule(self, rule):
        if not any(existing_rule.priority == rule.priority for existing_rule in self.rules):
            self.rules.append(rule)
            print(f"Rule successfully added. Total rules: {len(self.rules)}")
        else:
            print(f"Warning: Rule with priority {rule.priority} already exists. Rule {len(self.rules)+1} not added.")

    def add_fact(self, fact):
        self.facts[fact.name] = fact.value  # Store facts as name-value pairs

    def forward_chaining(self):
        triggered_rules = []
        new_fact_added = True
        while new_fact_added:
            new_fact_added = False
            # Sort rules by priority before evaluation
            sorted_rules = sorted(self.rules, key=lambda x: x.priority, reverse=True)
            for rule in sorted_rules:
                if rule.evaluate(self.facts) and rule.action not in self.facts:
                    self.facts[rule.action] = True
                    new_fact_added = True
                    triggered_rules.append(rule)
                    return [rule]
        return triggered_rules

    def backward_chaining(self, goal):
        if goal in self.facts:
            return self.facts[goal]
        # Sort rules by priority before evaluation
        sorted_rules = sorted(self.rules, key=lambda x: x.priority, reverse=True)
        for rule in sorted_rules:
            if rule.action == goal:
                if self.backward_chaining_helper(rule.condition):
                    self.facts[goal] = True
                    return True
        return self.handle_conflict(goal)

    def backward_chaining_helper(self, condition):
        if isinstance(condition, Condition):
            return condition.evaluate(self.facts)
        elif isinstance(condition, str):
            return self.backward_chaining(condition)
        else:
            return condition

    def handle_conflict(self, goal):
        conflicting_rules = [rule for rule in self.rules if rule.action == goal]
        if conflicting_rules:
            highest_priority_rule = max(conflicting_rules, key=lambda x: x.priority)
            if self.backward_chaining_helper(highest_priority_rule.condition):
                self.facts[goal] = True
                return True
        return False

################################################################################
################################################################################
######################### Coffee Recommendation System #########################
################################################################################
################################################################################

# Define facts
facts = [
    ("likes_strong", "Do you like strong coffee? (Y/N): "),
    ("likes_creamy", "Do you like creamy flavors? (Y/N): "),
    ("likes_sweet", "Do you like sweet flavors? (Y/N): "),
    ("needs_high_caffeine", "Do you need high caffeine? (Y/N): "),
    ("likes_mild", "Do you prefer mild flavors? (Y/N): "),
    ("likes_foam", "Do you like foam? (Y/N): "),
    ("likes_chocolate", "Do you like chocolate? (Y/N): ")
]

recommendations = ["recommend_espresso", "recommend_cappuccino", "recommend_latte", "recommend_mocha", 
                   "recommend_flat_white", "recommend_macchiato", "recommend_caramel_macchiato", "recommend_americano"]

# Define rules (with priorities)
rules = [
    (Condition(AND, "likes_strong", Condition(NOT, "likes_creamy")), recommendations[0], 12),
    (Condition(AND, "likes_creamy", "likes_foam"), recommendations[1], 11),
    (Condition(AND, "likes_creamy", Condition(NOT, "likes_foam")), recommendations[2], 10),
    (Condition(AND, "likes_sweet", "likes_chocolate"), recommendations[3], 9),
    (Condition(AND, "needs_high_caffeine", "likes_creamy", Condition(NOT, "likes_strong")), recommendations[4], 8),
    (Condition(AND, "needs_high_caffeine", Condition(NOT, "likes_creamy")), recommendations[5], 7),
    (Condition(AND, "likes_sweet", Condition(NOT, "likes_chocolate")), recommendations[6], 6),
    (Condition(OR, "likes_mild", Condition(NOT, "likes_strong")), recommendations[7], 5),
    (Condition(AND, "likes_strong", "likes_creamy"), recommendations[0], 4),
    (Condition(AND, "likes_sweet", "needs_high_caffeine"), recommendations[0], 1),
    (Condition(AND, "likes_mild", "likes_strong"), recommendations[0], 2),
    (Condition(AND, "likes_foam", Condition(NOT, "likes_creamy")), recommendations[1], 1)
]

# Create expert system and add rules and facts
coffee_expert_system = ExpertSystem()
for condition, action, priority in rules:
    coffee_expert_system.add_rule(Rule(condition, action, priority))

# Let the user input facts
for fact_name, question in facts:
    while True:
        user_input = input(question).strip().upper()
        if user_input in ['Y', 'N']:
            coffee_expert_system.add_fact(Fact(fact_name, user_input == 'Y'))
            break
        else:
            print("Please enter Y or N.")

# After running forward chaining
triggered_rules = coffee_expert_system.forward_chaining()

# Display recommendations
print("\nRecommendations based on your preferences:")
for rule in triggered_rules:
    coffee_type = rule.action.split('_')[1].replace('_', ' ').title()
    print(f"- {coffee_type}")

# Use backward chaining to check for specific recommendations
print("\nChecking specific recommendations:")

for recommendation in recommendations:
    if coffee_expert_system.backward_chaining(recommendation):
        coffee_type = recommendation.split('_')[1].replace('_', ' ').title()
        print(f"- {coffee_type} is recommended")
    else:
        coffee_type = recommendation.split('_')[1].replace('_', ' ').title()
        print(f"- {coffee_type} is not recommended")
