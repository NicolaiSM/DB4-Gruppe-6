from math import log


def voltagetempconv(reading):

    adc_V_lookup = [0.01852941, 0.02470588, 0.04941177, 0.05352942, 0.05764706, 0.06176471, 0.06485295, 0.06794118, 0.07102942, 0.07411765, 0.0782353, 0.08235294, 0.08647059, 0.08955883, 0.09264707, 0.0957353, 0.09882354, 0.1029412, 0.1070588, 0.1111765, 0.1152941, 0.1194118, 0.1235294, 0.1266177, 0.1297059, 0.1327941, 0.1358824, 0.14, 0.1441177, 0.1482353, 0.1513235, 0.1544118, 0.1575, 0.1605882, 0.1647059, 0.1688235, 0.1729412, 0.1760294, 0.1791177, 0.1822059, 0.1852941, 0.1894118, 0.1935294, 0.1976471, 0.2017647, 0.2058824, 0.21, 0.2141177, 0.2182353, 0.222353, 0.2254412, 0.2285294, 0.2316177, 0.2347059, 0.2388236, 0.2429412, 0.2470588, 0.2501471, 0.2532353, 0.2563236, 0.2594118, 0.2625, 0.2655883, 0.2686765, 0.2717647, 0.2758824, 0.28, 0.2841177, 0.2872059, 0.2902942, 0.2933824, 0.2964706, 0.2995588, 0.3026471, 0.3057353, 0.3088235, 0.3129412, 0.3170588, 0.3211765, 0.3252941, 0.3294118, 0.3335294, 0.3376471, 0.3417647, 0.3458824, 0.3489706, 0.3520588, 0.3551471, 0.3582353, 0.3613235, 0.3644118, 0.3675, 0.3705883, 0.3747059, 0.3788235, 0.3829412, 0.3870588, 0.3911765, 0.3952941, 0.3994118, 0.4035295, 0.4076471, 0.4107353, 0.4138236, 0.4169118, 0.42, 0.4241177, 0.4282353, 0.432353, 0.4354412, 0.4385294, 0.4416177, 0.4447059, 0.4488235, 0.4529412, 0.4570589, 0.4611764, 0.4652942, 0.4694118, 0.4725, 0.4755883, 0.4786765, 0.4817647, 0.4858823, 0.4900001, 0.4941177, 0.4961765, 0.4982353, 0.5002942, 0.502353, 0.5044117, 0.5064706, 0.5126471, 0.5188236, 0.5219118, 0.525, 0.5280883, 0.5311765, 0.5352941, 0.5394118, 0.5435295, 0.547647, 0.5517647, 0.5558824, 0.5583529, 0.5608235, 0.5632941, 0.5657647, 0.5682353, 0.5723529, 0.5764706, 0.5805883, 0.5847059, 0.5888236, 0.5929412, 0.5970588, 0.6011765, 0.6052941, 0.6094118, 0.6135294, 0.6176471, 0.6217647, 0.6258824, 0.63, 0.6324706, 0.6349412, 0.6374118, 0.6398824, 0.642353, 0.6464706, 0.6505883, 0.6547059, 0.6588235, 0.6629412, 0.6670588, 0.670147, 0.6732353, 0.6763235, 0.6794118, 0.6835294, 0.6876471, 0.6917647, 0.6948529, 0.6979412, 0.7010294, 0.7041177, 0.7082353, 0.712353, 0.7164706, 0.7195588, 0.7226471, 0.7257353, 0.7288236, 0.7319118, 0.735, 0.7380882, 0.7411765, 0.7452941, 0.7494118, 0.7535295, 0.7566176, 0.7597059, 0.7627941, 0.7658824, 0.77, 0.7741177, 0.7782353, 0.7807059, 0.7831765, 0.785647, 0.7881176, 0.7905883, 0.7947059, 0.7988235, 0.8029412, 0.8060294, 0.8091177, 0.8122059, 0.8152942, 0.8194118, 0.8235294, 0.8276471, 0.8307353, 0.8338236, 0.8369118, 0.8400001, 0.8441177, 0.8482353, 0.852353, 0.8554412, 0.8585295, 0.8616177, 0.8647059, 0.8677941, 0.8708824, 0.8739706, 0.8770589, 0.8811766, 0.8852942, 0.8894118, 0.8925, 0.8955883, 0.8986765, 0.9017648, 0.9058825, 0.91, 0.9141177, 0.9172059, 0.9202942, 0.9233824, 0.9264707, 0.9305883, 0.9347058, 0.9388236, 0.9412941, 0.9437648, 0.9462353, 0.948706, 0.9511765, 0.9542647, 0.957353, 0.9604412, 0.9635295, 0.9666177, 0.969706, 0.9727942, 0.9758824, 0.9820589, 0.9882354, 0.9923531, 0.9964705, 1.000588, 1.003677, 1.006765, 1.009853, 1.012941, 1.017059, 1.021176, 1.025294, 1.028382, 1.031471, 1.034559, 1.037647, 1.040735, 1.043824, 1.046912, 1.05, 1.054118, 1.058235, 1.062353, 1.066471, 1.070588, 1.074706, 1.077794, 1.080882, 1.083971, 1.087059, 1.090147, 1.093235, 1.096324, 1.099412, 1.1025, 1.105588, 1.108677, 1.111765, 1.115882, 1.12, 1.124118, 1.128235, 1.132353, 1.136471, 1.139559, 1.142647, 1.145735, 1.148824, 1.151912, 1.155, 1.158088, 1.161177, 1.165294, 1.169412, 1.17353, 1.177647, 1.181765, 1.185882, 1.188971, 1.192059, 1.195147, 1.198235, 1.202353, 1.206471, 1.210588, 1.213676, 1.216765, 1.219853, 1.222941, 1.227059, 1.231176, 1.235294, 1.239412, 1.243529, 1.247647, 1.250735, 1.253824, 1.256912, 1.26, 1.263088, 1.266176, 1.269265, 1.272353, 1.276471, 1.280588, 1.284706, 1.287794, 1.290882, 1.293971, 1.297059, 1.301177, 1.305294, 1.309412, 1.3125, 1.315588, 1.318676, 1.321765, 1.324853, 1.327941, 1.331029, 1.334118, 1.338235, 1.342353, 1.346471, 1.349559, 1.352647, 1.355735, 1.358824, 1.362941, 1.367059, 1.371176, 1.375294, 1.379412, 1.383529, 1.387647, 1.391765, 1.395882, 1.398353, 1.400824, 1.403294, 1.405765, 1.408235, 1.411324, 1.414412, 1.4175, 1.420588, 1.424706, 1.428824, 1.432941, 1.436029, 1.439118, 1.442206, 1.445294, 1.449412, 1.453529, 1.457647, 1.461765, 1.465882, 1.47, 1.472471, 1.474941, 1.477412, 1.479882, 1.482353, 1.488529, 1.494706, 1.497794, 1.500882, 1.503971, 1.507059, 1.510147, 1.513235, 1.516324, 1.519412, 1.5225, 1.525588, 1.528677, 1.531765, 1.535882, 1.54, 1.544118, 1.548235, 1.552353, 1.556471, 1.559559, 1.562647, 1.565735, 1.568824, 1.56955, 1.570277, 1.571003, 1.57173, 1.572457, 1.573183, 1.57391, 1.574637, 1.575363, 1.57609, 1.576817, 1.577543, 1.57827, 1.578997, 1.579723, 1.58045, 1.581177, 1.585294, 1.589412, 1.593529, 1.596618, 1.599706, 1.602794, 1.605882, 1.61, 1.614118, 1.618235, 1.621324, 1.624412, 1.6275, 1.630588, 1.634706, 1.638824, 1.642941, 1.646029, 1.649118, 1.652206, 1.655294, 1.658382, 1.661471, 1.664559, 1.667647, 1.671765, 1.675882, 1.68, 1.683088, 1.686177, 1.689265, 1.692353, 1.696471, 1.700588, 1.704706, 1.708824, 1.712941, 1.717059, 1.720147, 1.723235, 1.726324, 1.729412, 1.733529, 1.737647, 1.741765, 1.744853, 1.747941, 1.751029, 1.754118, 1.758235, 1.762353, 1.766471, 1.769559, 1.772647, 1.775735, 1.778824, 1.785, 1.791177, 1.793647, 1.796118, 1.798588, 1.801059, 1.80353, 1.807647, 1.811765, 1.815882, 1.818971, 1.822059, 1.825147, 1.828235, 1.831324, 1.834412, 1.8375, 1.840588, 1.844706, 1.848824, 1.852941, 1.85603, 1.859118, 1.862206, 1.865294, 1.869412, 1.87353, 1.877647, 1.880735, 1.883824, 1.886912, 1.89, 1.894118, 1.898235, 1.902353, 1.905441, 1.908529, 1.911618, 1.914706, 1.918823, 1.922941, 1.927059, 1.930147, 1.933235, 1.936324, 1.939412, 1.943529, 1.947647, 1.951765, 1.954853, 1.957941, 1.96103, 1.964118, 1.968235, 1.972353, 1.976471, 1.980588, 1.984706, 1.988824, 1.991912, 1.995, 1.998088, 2.001177, 2.005294, 2.009412, 2.01353, 2.016618, 2.019706, 2.022794, 2.025882, 2.03, 2.034118, 2.038235, 2.041324, 2.044412, 2.0475, 2.050588, 2.053677, 2.056765, 2.059853, 2.062941, 2.067059, 2.071177, 2.075294, 2.079412, 2.083529, 2.087647, 2.090735, 2.093824, 2.096912, 2.1, 2.103088, 2.106177, 2.109265, 2.112353, 2.116471, 2.120588, 2.124706, 2.127794, 2.130883, 2.133971, 2.137059, 2.141176, 2.145294, 2.149412, 2.1525, 2.155588, 2.158677, 2.161765, 2.165882, 2.17, 2.174118, 2.178235, 2.182353, 2.186471, 2.190588, 2.194706, 2.198824, 2.201912, 2.205, 2.208088, 2.211177, 2.214265, 2.217353, 2.220441, 2.22353, 2.227647, 2.231765, 2.235883, 2.238971, 2.242059, 2.245147, 2.248235, 2.251324, 2.254412, 2.2575, 2.260588, 2.263677, 2.266765, 2.269853, 2.272941, 2.27603, 2.279118, 2.282206, 2.285294, 2.288383, 2.291471, 2.294559, 2.297647, 2.301765, 2.305882, 2.31, 2.313088, 2.316177, 2.319265, 2.322353, 2.325441, 2.32853, 2.331618, 2.334706, 2.337794, 2.340883, 2.343971, 2.347059, 2.351177, 2.355294, 2.359412, 2.361882, 2.364353, 2.366824, 2.369294, 2.371765, 2.375882, 2.38, 2.384118, 2.387206, 2.390294, 2.393382, 2.396471, 2.399559, 2.402647, 2.405735, 2.408823, 2.412941, 2.417059, 2.421176, 2.423647, 2.426118, 2.428588, 2.431059, 2.433529, 2.437647, 2.441765, 2.445882, 2.448353, 2.450824, 2.453294, 2.455765, 2.458235, 2.462353, 2.466471, 2.470588, 2.473059, 2.475529, 2.478, 2.480471, 2.482941, 2.487059, 2.491177, 2.495294, 2.498382, 2.501471, 2.504559, 2.507647, 2.510735, 2.513824, 2.516912, 2.52, 2.523088, 2.526176, 2.529265, 2.532353, 2.535441, 2.538529, 2.541618, 2.544706, 2.547794, 2.550882, 2.553971, 2.557059, 2.561177, 2.565294, 2.569412, 2.5725, 2.575588, 2.578676, 2.581765, 2.584235, 2.586706, 2.589177, 2.591647, 2.594118, 2.597206, 2.600294, 2.603382, 2.606471, 2.608941, 2.611412, 2.613883, 2.616353, 2.618824, 2.621912, 2.625, 2.628088, 2.631176, 2.633647, 2.636118, 2.638588, 2.641059, 2.643529, 2.646, 2.648471, 2.650941, 2.653412, 2.655882, 2.658971, 2.662059, 2.665147, 2.668235, 2.670706, 2.673177, 2.675647, 2.678118, 2.680588, 2.683059, 2.685529, 2.688, 2.690471, 2.692941, 2.695412, 2.697882, 2.700353, 2.702824, 2.705294, 2.707765, 2.710235, 2.712706, 2.715177, 2.717647, 2.720118, 2.722588, 2.725059, 2.72753, 2.73, 2.733088, 2.736176, 2.739265, 2.742353, 2.744412, 2.746471, 2.748529, 2.750588, 2.752647, 2.754706, 2.758824, 2.762941, 2.767059, 2.769529, 2.772, 2.774471, 2.776941, 2.779412, 2.781471, 2.78353, 2.785588, 2.787647, 2.789706, 2.791765, 2.794853, 2.797941, 2.801029, 2.804118, 2.805882, 2.807647, 2.809412, 2.811176, 2.812941, 2.814706, 2.816471, 2.818941, 2.821412, 2.823883, 2.826353, 2.828824, 2.831912, 2.835, 2.838088, 2.841177, 2.843235, 2.845294, 2.847353, 2.849412, 2.851471, 2.853529, 2.855294, 2.857059, 2.858824, 2.860588, 2.862353, 2.864118, 2.865882, 2.868353, 2.870824, 2.873294, 2.875765, 2.878235, 2.880706, 2.883177, 2.885647, 2.888118, 2.890588, 2.892353, 2.894118, 2.895882, 2.897647, 2.899412, 2.901177, 2.902941, 2.905412, 2.907882, 2.910353, 2.912824, 2.915294, 2.917353, 2.919412, 2.921471, 2.92353, 2.925588, 2.927647, 2.929412, 2.931177, 2.932941, 2.934706, 2.936471, 2.938235, 2.94, 2.941765, 2.94353, 2.945294, 2.947059, 2.948823, 2.950588, 2.952353, 2.955441, 2.958529, 2.961618, 2.964706, 2.967176, 2.969647, 2.972118, 2.974588, 2.977059, 2.978824, 2.980588, 2.982353, 2.984118, 2.985882, 2.987647, 2.989412, 2.991177, 2.992941, 2.994706, 2.996471, 2.998235, 3.0, 3.001765, 3.003824, 3.005883, 3.007941, 3.01, 3.012059, 3.014118, 3.016177, 3.018235, 3.020294, 3.022353, 3.024412, 3.026471, 3.028235, 3.03, 3.031765, 3.03353, 3.035294, 3.037059, 3.038824, 3.040883, 3.042941, 3.045, 3.047059, 3.049118, 3.051177, 3.052941, 3.054706, 3.056471, 3.058235, 3.06, 3.061765, 3.063529, 3.065588, 3.067647, 3.069706, 3.071765, 3.073823, 3.075882, 3.077647, 3.079412, 3.081177, 3.082941, 3.084706, 3.086471, 3.088235, 3.09, 3.091765, 3.093529, 3.095294, 3.097059, 3.098824, 3.100588, 3.102133, 3.103677, 3.105221, 3.106765, 3.108309, 3.109853, 3.111397, 3.112941, 3.115, 3.117059, 3.119118, 3.121177, 3.123235, 3.125294, 3.126838, 3.128382, 3.129927, 3.131471, 3.133015, 3.134559, 3.136103, 3.137647, 3.139412, 3.141177, 3.142941, 3.144706, 3.146471, 3.148236, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15]

    NOM_RES = 10000
    SER_RES = 9820
    TEMP_NOM = 25
    THERM_B_COEFF = 3950
    ADC_MAX = 1023
    ADC_Vmax = 3.15

    raw_average = ADC_MAX * adc_V_lookup[round(reading)] / ADC_Vmax
    resistance = (SER_RES * raw_average) / (ADC_MAX - raw_average)

    steinhart = log(resistance / NOM_RES) / THERM_B_COEFF
    steinhart += 1.0 / (TEMP_NOM + 273.15)
    steinhart = (1.0 / steinhart) - 273.15
    return steinhart