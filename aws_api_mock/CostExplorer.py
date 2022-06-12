from calendar import day_abbr


class CostExplorer:

    def __init__(self):
        self.internals_data = {}

    def set_mock_count(self, mock_count: int):
        self.mock_count = mock_count
<<<<<<< HEAD

    def get_cost_and_usage(self, **params) -> dict:

        data_return = self.__get_values_with_params(params.get("Filter.Dimensions.Values.0"))

        return {
            "ResultsByTime": data_return,
            "DimensionValueAttributes": [],
            "ResponseMetadata": {
                "RequestId": "39cca693-3d86-031b-203c-f197033ba02c",
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "date": "Thu, 09 Jun 2017 10:47:16 GMT",
                    "content-type": "application/x-amz-json-1.1",
                    "content-length": "4688",
                    "connection": "keep-alive",
                    "x-amzn-requestid": "39cca693-3d86-031b-203c-f197033ba02c",
                    "cache-control": "no-cache"
                },
                "RetryAttempts": 0
            }
        }

    def __get_values_with_params(self, service = None):

=======

    def get_cost_and_usage(self, **params) -> dict:

        data_return = self.__get_values_with_params(params.get("Filter.Dimensions.Values.0"))

        return {
            "ResultsByTime": data_return,
            "DimensionValueAttributes": [],
            "ResponseMetadata": {
                "RequestId": "39cca693-3d86-031b-203c-f197033ba02c",
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "date": "Thu, 09 Jun 2017 10:47:16 GMT",
                    "content-type": "application/x-amz-json-1.1",
                    "content-length": "4688",
                    "connection": "keep-alive",
                    "x-amzn-requestid": "39cca693-3d86-031b-203c-f197033ba02c",
                    "cache-control": "no-cache"
                },
                "RetryAttempts": 0
            }
        }

    def __get_values_with_params(self, service = None):

        # print("------oi-------")

>>>>>>> wip
        serviceTranslationBag = {
            "tax": "Tax",
            "ec2": "EC2 - Other",
            "compute": "Amazon Elastic Compute Cloud - Compute",
            "s3": "Amazon Simple Storage Service",
            "workmail": "AmazonWorkMail",
            "cloudwatch": "AmazonCloudWatch",
            "sns": "Amazon Simple Notification Service",
            "route53": "Amazon Route 53",
            "rds": "Amazon Relational Database Service",
            "codecommit": "AWS CodeCommit",
            "dynamodb": "Amazon DynamoDB",
            "kms": "AWS Key Management Service",
            "cloudfront": "Amazon CloudFront",
            "efs": "Amazon Elastic File System",
            "ce": "AWS Cost Explorer"
        }

        base_raw_internals = {
            "2017-05-09": {
                "Tax": 0.07750604831243847,
                "EC2 - Other": 0.00023062766560844955,
                "Amazon Elastic Compute Cloud - Compute": 0.00023062766560844955,
                "Amazon Simple Storage Service": 0.06277746863558648,
                "AmazonWorkMail": 0.0005650859427642049,
                "AmazonCloudWatch": 0.01622120972822173,
                "Amazon Simple Notification Service": 0.33792137932933264,
                "Amazon Route 53": 0.00044697600173265045,
                "Amazon Relational Database Service": 0.0019059481681484788,
                "AWS CodeCommit": 0.0034959729024870434,
                "Amazon DynamoDB": 0.0026248906690162195,
                "AWS Key Management Service": 0.0016610571033699383,
                "Amazon CloudFront": 2.1378637410903408e-05,
                "Amazon Elastic File System": 0.0008907188622516529,
                "AWS Cost Explorer": 1.292191698499126e-06
            },
            "2017-05-10": {
                "Tax": 0.0270957561413653,
                "EC2 - Other": 0.2606873031952407,
                "Amazon Elastic Compute Cloud - Compute": 6.991959144333819e-05,
                "Amazon Simple Storage Service": 0.013362197214836651,
                "AmazonWorkMail": 0.0017843835819167377,
                "AmazonCloudWatch": 0.35781953456089244,
                "Amazon Simple Notification Service": 0.22200739727958446,
                "Amazon Route 53": 0.011544074348980738,
                "Amazon Relational Database Service": 0.030156378441861344,
                "AWS CodeCommit": 0.003198798955589783,
                "Amazon DynamoDB": 0.0065967739382003275,
                "AWS Key Management Service": 5.90082810675901e-05,
                "Amazon CloudFront": 0.000837491200090579,
                "Amazon Elastic File System": 0.002326208935844471,
                "AWS Cost Explorer": 0.00022346884799679583
            },
            "2017-05-11": {
                "Tax": 0.3716383862048105,
                "EC2 - Other": 0.0013544868433794071,
                "Amazon Elastic Compute Cloud - Compute": 0.0019787699609398485,
                "Amazon Simple Storage Service": 0.1863271395640563,
                "AmazonWorkMail": 0.014989036544669394,
                "AmazonCloudWatch": 0.08101186362064511,
                "Amazon Simple Notification Service": 0.006452084779391441,
                "Amazon Route 53": 0.028675412093054266,
                "Amazon Relational Database Service": 0.028675412093054266,
                "AWS CodeCommit": 0.08634450604532178,
                "Amazon DynamoDB": 0.015171487411262383,
                "AWS Key Management Service": 0.00029279515269651585,
                "Amazon CloudFront": 0.009717306916773654,
                "Amazon Elastic File System": 0.013094107931944828,
                "AWS Cost Explorer": 1.0036605315467037e-05
            },
            "2017-05-12": {
                "Tax": 0.00587164869451952,
                "EC2": 0.736754368657322,
                "Amazon Elastic Compute Cloud - Compute": 0.0541338762984979,
                "Amazon Simple Storage Service": 0.0253198289418126,
                "AmazonWorkMail": 0.00132222073376983,
                "AmazonCloudWatch": 0.000203127889969165,
                "Amazon Simple Notification Service": 0.00222109692636827,
                "Amazon Route 53": 0.00178406610111942,
                "Amazon Relational Database Service": 0.000428806746532002,
                "AWS CodeCommit": 3.15446211876148e-06,
                "Amazon DynamoDB": 0.000142014743730588,
                "AWS Key Management Service": 6.37980431704079e-05,
                "Amazon CloudFront": 2.50960903483979e-05,
                "Amazon Elastic File System": 6.13661984855237e-06,
                "AWS Cost Explorer": 0.000109675243509909
            },
            "2017-05-13": {
                "Tax": 0.0299832912632027,
                "EC2": 0.372927787199885,
                "Amazon Elastic Compute Cloud - Compute": 0.000797423115319135,
                "Amazon Simple Storage Service": 0.147615957271569,
                "AmazonWorkMail": 0.231040508438865,
                "AmazonCloudWatch": 0.0329626398249305,
                "Amazon Simple Notification Service": 0.00579219649437249,
                "Amazon Route 53": 0.0020068905186178,
                "Amazon Relational Database Service": 1.15841295916939e-05,
                "AWS CodeCommit": 0.00266443381913916,
                "Amazon DynamoDB": 0.000222039088770916,
                "AWS Key Management Service": 0.000294786357069851,
                "Amazon CloudFront": 0.00057829454181199,
                "Amazon Elastic File System": 8.9047393279388e-05,
                "AWS Cost Explorer": 6.03317401480726e-06
            },
            "2017-05-14": {
                "Tax": 0.737458871317735,
                "EC2": 0.13996597163107,
                "Amazon Elastic Compute Cloud - Compute": 0.00198089159142963,
                "Amazon Simple Storage Service": 0.0382445681771599,
                "AmazonWorkMail": 4.54488730488031e-06,
                "AmazonCloudWatch": 0.0149582152472998,
                "Amazon Simple Notification Service": 1.97992038796643e-05,
                "Amazon Route 53": 0.00309686533141503,
                "Amazon Relational Database Service": 9.59715924056206e-05,
                "AWS CodeCommit": 0.00132431120725637,
                "Amazon DynamoDB": 0.000947275659777033,
                "AWS Key Management Service": 2.60624525252578e-05,
                "Amazon CloudFront": 3.1653956449649e-06,
                "Amazon Elastic File System": 1.24017325872558e-05,
                "AWS Cost Explorer": 1.20325462618052e-05
            },
            "2017-05-15": {
                "Tax": 0.074842643694743,
                "EC2": 0.13228242402978,
                "Amazon Elastic Compute Cloud - Compute": 0.000420580586643783,
                "Amazon Simple Storage Service": 0.0322224514673983,
                "AmazonWorkMail": 0.0682424932031637,
                "AmazonCloudWatch": 0.0158979206696589,
                "Amazon Simple Notification Service": 0.360321525802614,
                "Amazon Route 53": 0.141266941704735,
                "Amazon Relational Database Service": 0.000671827985764775,
                "AWS CodeCommit": 0.00124725221193314,
                "Amazon DynamoDB": 0.00084680327724013,
                "AWS Key Management Service": 2.15787394733444e-05,
                "Amazon CloudFront": 5.56867512237478e-05,
                "Amazon Elastic File System": 6.381194232934e-06,
                "AWS Cost Explorer": 4.58397035579067e-06
            },
            "2017-05-16": {
                "Tax": 0.595264991985727,
                "EC2": 0.115540996885093,
                "Amazon Elastic Compute Cloud - Compute": 0.0418532304743227,
                "Amazon Simple Storage Service": 0.060338551443287,
                "AmazonWorkMail": 0.00645433680821152,
                "AmazonCloudWatch": 7.24410060169269e-06,
                "Amazon Simple Notification Service": 0.00145881089123798,
                "Amazon Route 53": 0.00478592161294431,
                "Amazon Relational Database Service": 0.00106468584481057,
                "AWS CodeCommit": 0.00022564277879068,
                "Amazon DynamoDB": 5.00412573679218e-05,
                "AWS Key Management Service": 0.000120886785353885,
                "Amazon CloudFront": 0.000207768482252608,
                "Amazon Elastic File System": 3.15222174444522e-05,
                "AWS Cost Explorer": 0.000832996639147523
            },
            "2017-05-17": {
                "Tax": 0.000576420331467799,
                "EC2": 0.165834114722552,
                "Amazon Elastic Compute Cloud - Compute": 0.229059552089792,
                "Amazon Simple Storage Service": 0.0152395278877266,
                "AmazonWorkMail": 0.1228783585259,
                "AmazonCloudWatch": 0.00567982893371378,
                "Amazon Simple Notification Service": 0.0383708494387319,
                "Amazon Route 53": 0.240125336394165,
                "Amazon Relational Database Service": 0.00516561630058797,
                "AWS CodeCommit": 0.00268869755346995,
                "Amazon DynamoDB": 0.00197987674496862,
                "AWS Key Management Service": 0.000340959737976411,
                "Amazon CloudFront": 0.000235923568808333,
                "Amazon Elastic File System": 7.98677974020386e-08,
                "AWS Cost Explorer": 5.48050675938945e-07
            },
            "2017-05-18": {
                "Tax": 0.000860992817200966,
                "EC2": 0.00516902388619041,
                "Amazon Elastic Compute Cloud - Compute": 0.102577544439013,
                "Amazon Simple Storage Service": 0.170561320097467,
                "AmazonWorkMail": 0.207268058041531,
                "AmazonCloudWatch": 0.0777822440291448,
                "Amazon Simple Notification Service": 0.226882921305569,
                "Amazon Route 53": 0.0177547664106568,
                "Amazon Relational Database Service": 0.00965442237407066,
                "AWS CodeCommit": 0.00591105075003731,
                "Amazon DynamoDB": 0.0034392082003655,
                "AWS Key Management Service": 2.54347135070538e-05,
                "Amazon CloudFront": 0.000183571739915512,
                "Amazon Elastic File System": 0.000191169013675179,
                "AWS Cost Explorer": 2.54659314354296e-06
            },
            "2017-05-19": {
                "Tax": 0.00800125611671711,
                "EC2": 0.454923102859853,
                "Amazon Elastic Compute Cloud - Compute": 0.123806510422326,
                "Amazon Simple Storage Service": 0.000746023929615768,
                "AmazonWorkMail": 0.0225150913290986,
                "AmazonCloudWatch": 0.131435086685371,
                "Amazon Simple Notification Service": 0.0259508379536798,
                "Amazon Route 53": 0.0193555714773395,
                "Amazon Relational Database Service": 0.0404324594107539,
                "AWS CodeCommit": 0.000909119496901459,
                "Amazon DynamoDB": 5.19972760952159e-05,
                "AWS Key Management Service": 2.46001976849282e-07,
                "Amazon CloudFront": 5.94654893666345e-05,
                "Amazon Elastic File System": 2.49007363561452e-10,
                "AWS Cost Explorer": 1.74939603640794e-06
            },
            "2017-05-20": {
                "Tax": 0.0171447947573601,
                "EC2": 0.947450564370959,
                "Amazon Elastic Compute Cloud - Compute": 0.013804833161357,
                "Amazon Simple Storage Service": 0.000119064280025234,
                "AmazonWorkMail": 0.00122685549525723,
                "AmazonCloudWatch": 0.00141819446177672,
                "Amazon Simple Notification Service": 0.000280365484378742,
                "Amazon Route 53": 0.00139944010223401,
                "Amazon Relational Database Service": 0.000411681670484437,
                "AWS CodeCommit": 6.89522693958713e-05,
                "Amazon DynamoDB": 0.000462413866518993,
                "AWS Key Management Service": 0.0042765041130639,
                "Amazon CloudFront": 0.000116774602256124,
                "Amazon Elastic File System": 1.24884017492558e-06,
                "AWS Cost Explorer": 0.000180978701743967
            },
            "2017-05-21": {
                "Tax": 0.513151207446984,
                "EC2": 0.000579854793031399,
                "Amazon Elastic Compute Cloud - Compute": 0.0866743435416319,
                "Amazon Simple Storage Service": 0.0167153325626347,
                "AmazonWorkMail": 0.127892556577315,
                "AmazonCloudWatch": 0.0651789714437303,
                "Amazon Simple Notification Service": 0.00587835061911844,
                "Amazon Route 53": 0.0001778438764311,
                "Amazon Relational Database Service": 0.011157785955582,
                "AWS CodeCommit": 0.000212586778489271,
                "Amazon DynamoDB": 2.50283279645596e-05,
                "AWS Key Management Service": 3.87817004328448e-05,
                "Amazon CloudFront": 1.69564241859605e-06,
                "Amazon Elastic File System": 9.90395643503023e-05,
                "AWS Cost Explorer": 1.27462991131288e-05
            },
            "2017-05-22": {
                "Tax": 0.0260859645177361,
                "EC2": 0.408090376870302,
                "Amazon Elastic Compute Cloud - Compute": 0.101343550916472,
                "Amazon Simple Storage Service": 0.160220838033877,
                "AmazonWorkMail": 0.0595577998793117,
                "AmazonCloudWatch": 0.0103997810560573,
                "Amazon Simple Notification Service": 0.00622600445385611,
                "Amazon Route 53": 0.00797527060649671,
                "Amazon Relational Database Service": 0.0134997660279513,
                "AWS CodeCommit": 0.0136802773779652,
                "Amazon DynamoDB": 0.0091260531965072,
                "AWS Key Management Service": 5.1933890306528e-07,
                "Amazon CloudFront": 0.00720881681020462,
                "Amazon Elastic File System": 0.0016520785686322,
                "AWS Cost Explorer": 0.000373767858158341
            },
            "2017-05-23": {
                "Tax": 0.213751926592738,
                "EC2": 0.172099780783149,
                "Amazon Elastic Compute Cloud - Compute": 0.00489025135784771,
                "Amazon Simple Storage Service": 2.92099938364655e-05,
                "AmazonWorkMail": 0.00552489397924033,
                "AmazonCloudWatch": 0.215522648813839,
                "Amazon Simple Notification Service": 0.0117002974361147,
                "Amazon Route 53": 0.0206720619948709,
                "Amazon Relational Database Service": 0.0152543607293898,
                "AWS CodeCommit": 0.00110739812850285,
                "Amazon DynamoDB": 0.0122795802395673,
                "AWS Key Management Service": 0.00855353246550534,
                "Amazon CloudFront": 0.0541247582590789,
                "Amazon Elastic File System": 0.0319423123418065,
                "AWS Cost Explorer": 0.00094270079281584
            },
            "2017-05-24": {
                "Tax": 0.779959671450317,
                "EC2": 0.0172139665451165,
                "Amazon Elastic Compute Cloud - Compute": 0.000425086977117722,
                "Amazon Simple Storage Service": 0.0241127439527929,
                "AmazonWorkMail": 3.73250244718355e-06,
                "AmazonCloudWatch": 0.000166491397861508,
                "Amazon Simple Notification Service": 0.000632852084929923,
                "Amazon Route 53": 0.0038877811880861,
                "Amazon Relational Database Service": 6.35818704471511e-05,
                "AWS CodeCommit": 0.000656824606158269,
                "Amazon DynamoDB": 0.000340876416533768,
                "AWS Key Management Service": 0.000493951955809984,
                "Amazon CloudFront": 0.000112376893659365,
                "Amazon Elastic File System": 7.02979825627315e-05,
                "AWS Cost Explorer": 2.42708511553947e-05
            },
            "2017-05-25": {
                "Tax": 0.209090410036343,
                "EC2": 0.572846137118067,
                "Amazon Elastic Compute Cloud - Compute": 0.013348695850936,
                "Amazon Simple Storage Service": 0.0211725637955592,
                "AmazonWorkMail": 0.00141757781513469,
                "AmazonCloudWatch": 0.00288589135551213,
                "Amazon Simple Notification Service": 0.00633704763230209,
                "Amazon Route 53": 0.000171861414626926,
                "Amazon Relational Database Service": 7.04387755955099e-05,
                "AWS CodeCommit": 0.000591925798227896,
                "Amazon DynamoDB": 4.84514614237404e-06,
                "AWS Key Management Service": 7.03830028788781e-06,
                "Amazon CloudFront": 0.000311586343567646,
                "Amazon Elastic File System": 5.39394417463866e-05,
                "AWS Cost Explorer": 1.62464259906234e-11
            },
            "2017-05-26": {
                "Tax": 0.0763768880472465,
                "EC2": 0.749221990697646,
                "Amazon Elastic Compute Cloud - Compute": 0.000282283001819282,
                "Amazon Simple Storage Service": 0.000240138143148054,
                "AmazonWorkMail": 0.000618942908127698,
                "AmazonCloudWatch": 0.000542754052498301,
                "Amazon Simple Notification Service": 5.04211588770161e-05,
                "Amazon Route 53": 1.40220911014923e-05,
                "Amazon Relational Database Service": 1.80273121803195e-06,
                "AWS CodeCommit": 4.22304949848479e-05,
                "Amazon DynamoDB": 4.37296353807578e-06,
                "AWS Key Management Service": 1.21256419770993e-05,
                "Amazon CloudFront": 3.99612287435612e-06,
                "Amazon Elastic File System": 0.000191364753821333,
                "AWS Cost Explorer": 0.000412930255458268
            },
            "2017-05-27": {
                "Tax": 0.272494494559865,
                "EC2": 0.136103569929197,
                "Amazon Elastic Compute Cloud - Compute": 2.44307455934785e-05,
                "Amazon Simple Storage Service": 0.0442844882498305,
                "AmazonWorkMail": 0.363054263479301,
                "AmazonCloudWatch": 0.00569604881885216,
                "Amazon Simple Notification Service": 0.0010011426722497,
                "Amazon Route 53": 4.6850595436832e-05,
                "Amazon Relational Database Service": 5.61114192514975e-05,
                "AWS CodeCommit": 0.000873201728150045,
                "Amazon DynamoDB": 0.00252617452466442,
                "AWS Key Management Service": 0.000396852398086624,
                "Amazon CloudFront": 0.0016222706874019,
                "Amazon Elastic File System": 8.13879832077479e-05,
                "AWS Cost Explorer": 1.90707002802881e-06
            },
            "2017-05-28": {
                "Tax": 0.800165459357284,
                "EC2": 0.0252042938753547,
                "Amazon Elastic Compute Cloud - Compute": 0.170569033141787,
                "Amazon Simple Storage Service": 0.0254327723940399,
                "AmazonWorkMail": 0.00382357330872912,
                "AmazonCloudWatch": 0.000111902061238004,
                "Amazon Simple Notification Service": 0.000162339399779177,
                "Amazon Route 53": 1.52657214948244e-05,
                "Amazon Relational Database Service": 1.91398598894456e-10,
                "AWS CodeCommit": 6.46939993507601e-05,
                "Amazon DynamoDB": 2.55397245727813e-05,
                "AWS Key Management Service": 2.09834475694907e-06,
                "Amazon CloudFront": 1.33448278497673e-05,
                "Amazon Elastic File System": 5.74274284161334e-06,
                "AWS Cost Explorer": 1.40988940227305e-06
            },
            "2017-05-29": {
                "Tax": 0.0311507917467185,
                "EC2": 0.113563735642959,
                "Amazon Elastic Compute Cloud - Compute": 0.0590298142545421,
                "Amazon Simple Storage Service": 0.151926014943913,
                "AmazonWorkMail": 0.0603322799703922,
                "AmazonCloudWatch": 0.00510197985223178,
                "Amazon Simple Notification Service": 0.0379471409555634,
                "Amazon Route 53": 0.048328369472868,
                "Amazon Relational Database Service": 0.0374768393372464,
                "AWS CodeCommit": 0.0862761628611473,
                "Amazon DynamoDB": 0.116677584924845,
                "AWS Key Management Service": 0.0914432484740491,
                "Amazon CloudFront": 0.00976150176865023,
                "Amazon Elastic File System": 0.0186947797965006,
                "AWS Cost Explorer": 0.0171222945247314
            },
            "2017-05-30": {
                "Tax": 0.244923581768557,
                "EC2": 0.0439657425684782,
                "Amazon Elastic Compute Cloud - Compute": 0.963280932195269,
                "Amazon Simple Storage Service": 0.036736752038052,
                "AmazonWorkMail": 0.0102139676093596,
                "AmazonCloudWatch": 0.0266808298172474,
                "Amazon Simple Notification Service": 0.000120204376137063,
                "Amazon Route 53": 0.00315196544790421,
                "Amazon Relational Database Service": 0.000364726578954787,
                "AWS CodeCommit": 0.014209867286072,
                "Amazon DynamoDB": 3.33613321308984e-05,
                "AWS Key Management Service": 9.34072072171345e-07,
                "Amazon CloudFront": 2.07464733796659e-07,
                "Amazon Elastic File System": 2.80596293897754e-06,
                "AWS Cost Explorer": 5.64151150641281e-08
            },
            "2017-05-31": {
                "Tax": 0.0247880785784552,
                "EC2": 0.00108680032053173,
                "Amazon Elastic Compute Cloud - Compute": 0.0108177878449217,
                "Amazon Simple Storage Service": 0.200499856423063,
                "AmazonWorkMail": 0.143689879608654,
                "AmazonCloudWatch": 0.000633934999215201,
                "Amazon Simple Notification Service": 0.310703411579247,
                "Amazon Route 53": 0.000231724128678944,
                "Amazon Relational Database Service": 0.0568326044466414,
                "AWS CodeCommit": 0.0921865365385506,
                "Amazon DynamoDB": 0.0171438520048548,
                "AWS Key Management Service": 0.0339524721069452,
                "Amazon CloudFront": 0.00354867693555138,
                "Amazon Elastic File System": 0.000519244741173442,
                "AWS Cost Explorer": 0.00558211423291453
            },
            "2017-06-01": {
                "Tax": 0.0298652504548833,
                "EC2": 1.78297751430096,
                "Amazon Elastic Compute Cloud - Compute": 0.0873439490114476,
                "Amazon Simple Storage Service": 0.506950754281554,
                "AmazonWorkMail": 0.0773776905344538,
                "AmazonCloudWatch": 0.0104703597844603,
                "Amazon Simple Notification Service": 0.000450113252384039,
                "Amazon Route 53": 0.0122536115916742,
                "Amazon Relational Database Service": 0.00124257131134961,
                "AWS CodeCommit": 0.000770741407846975,
                "Amazon DynamoDB": 0.00199509888656228,
                "AWS Key Management Service": 0.00150995716508994,
                "Amazon CloudFront": 0.00215898347571578,
                "Amazon Elastic File System": 0.000907442948254195,
                "AWS Cost Explorer": 3.45809516389208e-05
            },
            "2017-06-02": {
                "Tax": 0.00358541015637396,
                "EC2": 0.0181198066551955,
                "Amazon Elastic Compute Cloud - Compute": 0.731698412406645,
                "Amazon Simple Storage Service": 0.00823188262370141,
                "AmazonWorkMail": 0.243357116347546,
                "AmazonCloudWatch": 0.000432528568027389,
                "Amazon Simple Notification Service": 0.000545422585366071,
                "Amazon Route 53": 8.01002502995449e-05,
                "Amazon Relational Database Service": 0.00012882138157974,
                "AWS CodeCommit": 0.00109604863481463,
                "Amazon DynamoDB": 0.00108581059924538,
                "AWS Key Management Service": 0.000872354459957073,
                "Amazon CloudFront": 0.00166260971824988,
                "Amazon Elastic File System": 4.20669000589053e-05,
                "AWS Cost Explorer": 4.06072936093834e-06
            },
            "2017-06-03": {
                "Tax": 0.00186941348963873,
                "EC2": 0.296201436287152,
                "Amazon Elastic Compute Cloud - Compute": 0.0159227285645666,
                "Amazon Simple Storage Service": 0.289023351607094,
                "AmazonWorkMail": 0.251229973781939,
                "AmazonCloudWatch": 0.0680848303345711,
                "Amazon Simple Notification Service": 0.00509144624313619,
                "Amazon Route 53": 0.0342550530994418,
                "Amazon Relational Database Service": 0.00434510577756962,
                "AWS CodeCommit": 0.00370828712291205,
                "Amazon DynamoDB": 0.00250688282329943,
                "AWS Key Management Service": 0.000330565569672972,
                "Amazon CloudFront": 0.000117983194177711,
                "Amazon Elastic File System": 5.87447565005009e-05,
                "AWS Cost Explorer": 6.37245742596346e-05
            },
            "2017-06-04": {
                "Tax": 0.145180817763851,
                "EC2": 0.051611708821735,
                "Amazon Elastic Compute Cloud - Compute": 0.562354423203855,
                "Amazon Simple Storage Service": 0.292836777503652,
                "AmazonWorkMail": 0.0153817399494869,
                "AmazonCloudWatch": 0.000509666764583432,
                "Amazon Simple Notification Service": 5.85771616829714e-05,
                "Amazon Route 53": 0.00659198457305449,
                "Amazon Relational Database Service": 0.000123581269700523,
                "AWS CodeCommit": 0.00143231247785618,
                "Amazon DynamoDB": 2.95802347128848e-06,
                "AWS Key Management Service": 0.000307412650750984,
                "Amazon CloudFront": 7.85283279514292e-05,
                "Amazon Elastic File System": 0.000142484868131175,
                "AWS Cost Explorer": 0.001042087166911
            },
            "2017-06-05": {
                "Tax": 0.746787557499429,
                "EC2": 0.0251479115594533,
                "Amazon Elastic Compute Cloud - Compute": 0.0781158201597665,
                "Amazon Simple Storage Service": 0.0203272990824157,
                "AmazonWorkMail": 0.000396202080196234,
                "AmazonCloudWatch": 4.67933560591179e-05,
                "Amazon Simple Notification Service": 0.000425410821757138,
                "Amazon Route 53": 0.000510724673465761,
                "Amazon Relational Database Service": 0.00110809943102831,
                "AWS CodeCommit": 0.000268178436261336,
                "Amazon DynamoDB": 8.99667273587417e-05,
                "AWS Key Management Service": 0.000935856571105112,
                "Amazon CloudFront": 0.00290116786147282,
                "Amazon Elastic File System": 1.46304968004013e-05,
                "AWS Cost Explorer": 3.67628321015252e-05
            },
            "2017-06-06": {
                "Tax": 0.0379553607558004,
                "EC2": 0.875817006204726,
                "Amazon Elastic Compute Cloud - Compute": 0.0155164172724193,
                "Amazon Simple Storage Service": 0.00404239412429527,
                "AmazonWorkMail": 1.35962526070094e-05,
                "AmazonCloudWatch": 0.00135937439112739,
                "Amazon Simple Notification Service": 0.00328380578156049,
                "Amazon Route 53": 0.00236566381817789,
                "Amazon Relational Database Service": 0.00114522846493341,
                "AWS CodeCommit": 6.2127761690271e-07,
                "Amazon DynamoDB": 0.00012841699263347,
                "AWS Key Management Service": 9.57009700853296e-06,
                "Amazon CloudFront": 1.56914122461707e-05,
                "Amazon Elastic File System": 0.000130410972325797,
                "AWS Cost Explorer": 4.49116569152967e-06
            },
            "2017-06-07": {
                "Tax": 0.0904749767089096,
                "EC2": 0.700872576477453,
                "Amazon Elastic Compute Cloud - Compute": 0.00557164722950508,
                "Amazon Simple Storage Service": 0.0540581883453801,
                "AmazonWorkMail": 0.103944239076199,
                "AmazonCloudWatch": 0.00203004911500356,
                "Amazon Simple Notification Service": 0.016271539261587,
                "Amazon Route 53": 0.0195745383739334,
                "Amazon Relational Database Service": 0.00013285871371537,
                "AWS CodeCommit": 3.66008776245535e-05,
                "Amazon DynamoDB": 4.15659952499569e-06,
                "AWS Key Management Service": 5.54916798855286e-07,
                "Amazon CloudFront": 2.29587405839342e-07,
                "Amazon Elastic File System": 1.11000385585348e-06,
                "AWS Cost Explorer": 1.25629777586883e-07
            },
            "2017-06-08": {
                "Tax": 0.164437101259923,
                "EC2": 0.383481991065009,
                "Amazon Elastic Compute Cloud - Compute": 0.000626032177027275,
                "Amazon Simple Storage Service": 0.0436371651091275,
                "AmazonWorkMail": 0.000946919732537033,
                "AmazonCloudWatch": 0.000174428601147462,
                "Amazon Simple Notification Service": 0.00044479920513563,
                "Amazon Route 53": 0.000671230221507764,
                "Amazon Relational Database Service": 0.0015076597274628,
                "AWS CodeCommit": 3.89432259795261e-06,
                "Amazon DynamoDB": 5.90377245547888e-05,
                "AWS Key Management Service": 3.01475288239731e-06,
                "Amazon CloudFront": 1.68357009821596e-08,
                "Amazon Elastic File System": 5.51543940321717e-09,
                "AWS Cost Explorer": 3.26451174300368e-08
            }
        }
        
        base_result_by_time = [
            {
                "TimePeriod": {
                    "Start": "2017-05-09",
                    "End": "2017-05-10"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-09"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-10",
                    "End": "2017-05-11"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-10"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-11",
                    "End": "2017-05-12"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-11"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-12",
                    "End": "2017-05-13"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-12"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-13",
                    "End": "2017-05-14"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-13"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-14",
                    "End": "2017-05-15"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-14"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-15",
                    "End": "2017-05-16"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-15"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-16",
                    "End": "2017-05-17"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-16"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-17",
                    "End": "2017-05-18"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-17"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-18",
                    "End": "2017-05-19"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-18"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-19",
                    "End": "2017-05-20"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-19"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-20",
                    "End": "2017-05-21"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-20"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-21",
                    "End": "2017-05-22"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-21"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-22",
                    "End": "2017-05-23"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-22"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-23",
                    "End": "2017-05-24"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-23"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-24",
                    "End": "2017-05-25"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-24"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-25",
                    "End": "2017-05-26"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-25"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-26",
                    "End": "2017-05-27"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-26"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-27",
                    "End": "2017-05-28"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-27"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-28",
                    "End": "2017-05-29"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-28"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-29",
                    "End": "2017-05-30"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-29"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-30",
                    "End": "2017-05-31"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-30"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-05-31",
                    "End": "2017-06-01"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-05-31"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": False
            },
            {
                "TimePeriod": {
                    "Start": "2017-06-01",
                    "End": "2017-06-02"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-06-01"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": True
            },
            {
                "TimePeriod": {
                    "Start": "2017-06-02",
                    "End": "2017-06-03"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-06-02"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": True
            },
            {
                "TimePeriod": {
                    "Start": "2017-06-03",
                    "End": "2017-06-04"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-06-03"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": True
            },
            {
                "TimePeriod": {
                    "Start": "2017-06-04",
                    "End": "2017-06-05"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-06-04"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": True
            },
            {
                "TimePeriod": {
                    "Start": "2017-06-05",
                    "End": "2017-06-06"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-06-05"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": True
            },
            {
                "TimePeriod": {
                    "Start": "2017-06-06",
                    "End": "2017-06-07"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-06-06"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": True
            },
            {
                "TimePeriod": {
                    "Start": "2017-06-07",
                    "End": "2017-06-08"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-06-07"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": True
            },
            {
                "TimePeriod": {
                    "Start": "2017-06-08",
                    "End": "2017-06-09"
                },
                "Total": {
                    "BlendedCost": {
                        "Amount": self.__build_result_by_time_payload(base_raw_internals["2017-06-08"], service),
                        "Unit": "USD"
                    }
                },
                "Groups": [],
                "Estimated": True
            }
        ]

        for entry in base_result_by_time:
            key_to_search = entry["TimePeriod"]["Start"]
            if key_to_search in base_raw_internals:
                data_group = base_raw_internals[key_to_search]
                day_sum = 0
                for internal_day_data in data_group:
                    value_to_sum = data_group[internal_day_data]
                    day_sum += value_to_sum

        return base_result_by_time[:self.mock_count]

<<<<<<< HEAD
    def __build_result_by_time_payload(self) -> dict:
        return {}
=======
    def __build_result_by_time_payload(self, dayData: dict, service = None) -> dict:

        if not service:
            day_summed = 0
            for singleServiceDataKey in dayData:
                day_summed += dayData[singleServiceDataKey]
            return day_summed

        return dayData[service]
>>>>>>> wip
