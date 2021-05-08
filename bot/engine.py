from experta import *
import json
import sys

list_disease = []
symptom_disease = {}
info_disease = {}

def load_data():
	global list_disease,symptom_disease,info_disease
	with open("bot/diseaseDict.json", 'r') as sd:
		temp_smap = sd.read()
		symptom_disease = json.loads(temp_smap)
		for key, values in symptom_disease.items():
			list_disease.append(values)
	for disease in list_disease:
		with open("bot/Disease Descriptions and Treatments/" + disease + ".txt") as ddt:
			disease_s_data = ddt.read()
			info_disease[disease] = disease_s_data

def disease_named(matched_disease):
	print(matched_disease+".")
	matched_disease_info = info_disease[matched_disease]
	print(matched_disease_info+"\n")

class StartEngine(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		yield Fact(action = "match_disease")
	@Rule(Fact(action='match_disease'),
			NOT(Fact(headache=W())),
			salience = 1)
	def symptom_0(self):
		self.declare(Fact(headache=sys.argv[1]))

	@Rule(Fact(action='match_disease'),
			NOT(Fact(back_pain=W())),
			salience = 1)
	def symptom_back_pain(self):
		self.declare(Fact(back_pain=sys.argv[2]))

	@Rule(Fact(action='match_disease'),
			NOT(Fact(chest_pain=W())),
			salience = 1)
	def symptom_chest_pain(self):
		self.declare(Fact(chest_pain=sys.argv[3]))

	@Rule(Fact(action='match_disease'),
			NOT(Fact(cough=W())),
			salience = 1)
	def symptom_cough(self):
		self.declare(Fact(cough=sys.argv[4]))

	@Rule(Fact(action='match_disease'),
			NOT(Fact(fainting=W())),
			salience = 1)
	def symptom_fainting(self):
		self.declare(Fact(fainting=sys.argv[5]))

	@Rule(Fact(action='match_disease'),
			NOT(Fact(fatigue=W())),
			salience = 1)
	def symptom_fatigue(self):
		self.declare(Fact(fatigue=sys.argv[6]))
	 
	@Rule(Fact(action='match_disease'),
			NOT(Fact(sunken_eyes=W())),
			salience = 1)
	def symptom_sunken_eyes(self):
		self.declare(Fact(sunken_eyes=sys.argv[7]))
	
	@Rule(Fact(action='match_disease'),
			NOT(Fact(low_body_temp=W())),
			salience = 1)
	def symptom_low_body_temp(self):
		self.declare(Fact(low_body_temp=sys.argv[8]))
	
	@Rule(Fact(action='match_disease'),
			NOT(Fact(restlessness=W())),
			salience = 1)
	def symptom_restlessness(self):
		self.declare(Fact(restlessness=sys.argv[9]))
	
	@Rule(Fact(action='match_disease'),
			NOT(Fact(sore_throat=W())),
			salience = 1)
	def symptom_sore_throat(self):
		self.declare(Fact(sore_throat=sys.argv[10]))
	
	@Rule(Fact(action='match_disease'),
			NOT(Fact(fever=W())),
			salience = 1)
	def symptom_fever(self):
		self.declare(Fact(fever=sys.argv[11]))

	@Rule(Fact(action='match_disease'),
			NOT(Fact(nausea=W())),
			salience = 1)
	def symptom_nausea(self):
		self.declare(Fact(nausea=sys.argv[12]))

	@Rule(Fact(action='match_disease'),
			NOT(Fact(blurred_vision=W())),
			salience = 1)
	def symptom_blurred_vision(self):
		self.declare(Fact(blurred_vision=sys.argv[13]))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '0'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '0'),
			Fact(cough = '0'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '1'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '1'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '1'),
			Fact(blurred_vision = '0'))
	def disease_Jaundice(self):
		self.declare(Fact(disease = "Jaundice"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '0'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '0'),
			Fact(cough = '0'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '0'),
			Fact(restlessness = '1'),
			Fact(low_body_temp = '0'),
			Fact(fever = '0'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '0'),
			Fact(blurred_vision = '0'))
	def disease_Alzheimers(self):
		self.declare(Fact(disease = "Alzheimers"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '0'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '1'),
			Fact(cough = '1'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '0'),
			Fact(restlessness = '1'),
			Fact(low_body_temp = '0'),
			Fact(fever = '0'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '0'),
			Fact(blurred_vision = '0'))
	def disease_Asthma(self):
		self.declare(Fact(disease = "Asthma"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '0'),
			Fact(back_pain = '1'),
			Fact(chest_pain = '0'),
			Fact(cough = '0'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '1'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '0'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '0'),
			Fact(blurred_vision = '0'))
	def disease_Arthritis(self):
		self.declare(Fact(disease = "Arthritis"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '0'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '1'),
			Fact(cough = '1'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '0'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '1'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '0'),
			Fact(blurred_vision = '0'))
	def disease_Tuberculosis(self):
		self.declare(Fact(disease = "Tuberculosis"))



	@Rule(  Fact(action='match_disease'),
			Fact(headache = '1'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '0'),
			Fact(cough = '1'),
			Fact(fainting = '0'),
			Fact(sore_throat = '1'),
			Fact(fatigue = '0'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '1'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '0'),
			Fact(blurred_vision = '0'))
	def disease_Sinusitis(self):
		self.declare(Fact(disease = "Sinusitis"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '0'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '0'),
			Fact(cough = '0'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '1'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '0'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '0'),
			Fact(blurred_vision = '0'))
	def disease_Epilepsy(self):
		self.declare(Fact(disease = "Epilepsy"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '0'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '1'),
			Fact(cough = '0'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '0'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '0'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '1'),
			Fact(blurred_vision = '0'))
	def disease_Heart(self):
		self.declare(Fact(disease = "Heart Disease"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '0'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '0'),
			Fact(cough = '0'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '1'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '0'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '1'),
			Fact(blurred_vision = '1'))
	def disease_Diabetes(self):
		self.declare(Fact(disease = "Diabetes"))

	@Rule(  Fact(action='match_disease'),
		Fact(headache = '0'),
		Fact(back_pain = '0'),
		Fact(chest_pain = '0'),
		Fact(cough = '0'),
		Fact(fainting = '1'),
		Fact(sore_throat = '0'),
		Fact(fatigue = '0'),
		Fact(restlessness = '0'),
		Fact(low_body_temp = '1'),
		Fact(fever = '0'),
		Fact(sunken_eyes = '0'),
		Fact(nausea = '0'),
		Fact(blurred_vision = '0'))
	def disease_Hypothermia(self):
		self.declare(Fact(disease = "Hypothermia"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '1'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '0'),
			Fact(cough = '0'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '0'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '0'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '1'),
			Fact(blurred_vision = '1'))
	def disease_Glaucoma(self):
		self.declare(Fact(disease = "Glaucoma"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '0'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '0'),
			Fact(cough = '0'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '1'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '0'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '1'),
			Fact(blurred_vision = '0'))
	def disease_Hyperthyroidism(self):
		self.declare(Fact(disease = "Hyperthyroidism"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '0'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '0'),
			Fact(cough = '0'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '1'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '0'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '1'),
			Fact(blurred_vision = '1'))
	def disease_Diabetes(self):
		self.declare(Fact(disease = "Diabetes"))

	@Rule(  Fact(action='match_disease'),
			Fact(headache = '1'),
			Fact(back_pain = '0'),
			Fact(chest_pain = '0'),
			Fact(cough = '0'),
			Fact(fainting = '0'),
			Fact(sore_throat = '0'),
			Fact(fatigue = '0'),
			Fact(restlessness = '0'),
			Fact(low_body_temp = '0'),
			Fact(fever = '1'),
			Fact(sunken_eyes = '0'),
			Fact(nausea = '1'),
			Fact(blurred_vision = '0'))
	def disease_Heat(self):
		self.declare(Fact(disease = "Heat Stroke"))



	@Rule(  Fact(action='match_disease'),
			Fact(disease=MATCH.disease),
			salience = -2)
	def disease(self, disease):
		print(1)
		print(disease+".")
		disease = info_disease[disease]
		print(disease+"\n")

	@Rule(  Fact(action='match_disease'),
			Fact(headache=MATCH.headache),
			Fact(back_pain=MATCH.back_pain),
			Fact(chest_pain=MATCH.chest_pain),
			Fact(cough=MATCH.cough),
			Fact(fainting=MATCH.fainting),
			Fact(sore_throat=MATCH.sore_throat),
			Fact(fatigue=MATCH.fatigue),
			Fact(low_body_temp=MATCH.low_body_temp),
			Fact(restlessness=MATCH.restlessness),
			Fact(fever=MATCH.fever),
			Fact(sunken_eyes=MATCH.sunken_eyes),
			Fact(nausea=MATCH.nausea),
			Fact(blurred_vision=MATCH.blurred_vision),NOT(Fact(disease=MATCH.disease)),
			salience = -2)

	def not_matched(self,headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision):
		simp_list = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision]
		no_simp = 0
		for i in range(0,len(simp_list)):
			if(simp_list[i] == '0'):
				no_simp = no_simp + 1
		if(no_simp == len(simp_list)):
			print(0)
			return
		print(2)
		max_disease = ""
		min_heuristic = 100000000000
		for key,val in symptom_disease.items():
			count = 0
			heuristic = 0
			temp_simp = eval(key)
			for i in range(0,len(simp_list)):
				if(temp_simp[i] == '0'):
					heuristic=heuristic+2.0*(int(simp_list[i]))
				elif(simp_list[i] == '0'):
					heuristic=heuristic+0.5*(int(temp_simp[i]))
				else:
					heuristic=heuristic+1.0*(abs(int(temp_simp[i])-int(simp_list[i])))
			if heuristic<min_heuristic:
				max_disease = val
				min_heuristic=heuristic
		disease_named(max_disease)
if __name__ == "__main__":
	load_data()
	engine = StartEngine()
	engine.reset()
	engine.run()
	
	