class Mercs():

    def merc_num(merc_name):

        merc_choice = str.lower(merc_name)
        mercs = {
            "peasant warrior" : str(1),
            "militia warrior" : str(2),
            "peasant warrioress" : str(3),
            "militia warrioress" : str(4),
            "peasant leader" : str(5),
            "militia leader" : str(6),
            "militia maiden" : str(7),
            "peasant maiden" : str(8),
            "ironclaw thief" : str(9),
            "ironclaw brigand" : str(10),
            "hook thief" : str(11),
            "hook brigand" : str(12),
            "goblin warrior" : str(13),
            "goblin marauder" : str(14),
            "goblin raider" : str(15),
            "goblin archer" : str(16),
            "goblin hunter" : str(17),
            "goblin chaser" : str(18),
            "orc marauder" : str(19),
            "orc destroyer" : str(20),
            "ruffian" : str(21),
            "shield ruffian" : str(22),
            "brawling cook" : str(23),
            "fighter cook" : str(24),
            "zombie" : str(25),
            "walking corpse" : str(26),
            "skeleton pawn" : str(27),
            "slave skeleton" : str(28),
            "britain" : str(29),
            "junior knight" : str(30),
            "page" : str(31),
            "rosa" : str(32),
            "mercedes" : str(33),
            "helena" : str(34),
            "noel" : str(35),
            "marlene" : str(36),
            "pierre" : str(37),
            "trainee knight" : str(38),
            "ghoul pawn" : str(39),
            "plague ghoul" : str(40),
            "catapult geezer" : str(41),
            "claudia" : str(42),
            "devil hound" : str(43),
            "glacial hound" : str(44),
            "hellhound" : str(45),
            "lizard warrior" : str(46),
            "lizard marauder" : str(47),
            "lizard hunter" : str(48),
            "veteran thief" : str(49),
            "veteran brigand" : str(50),
            "wiggle" : str(51),
            "bran" : str(52),
            "royal knight" : str(53),
            "karg" : str(54),
            "black knight" : str(55),
            "arlos" : str(57),
            "miné" : str(58),
            "tiara" : str(59),
            "joseph" : str(61),
            "kaci" : str(63),
            "agony undead" : str(64),
            "frost undead" : str(65),
            "venom undead" : str(66),
            "cordelia" : str(67),
            "velona" : str(68),
            "elaine" : str(69),
            "cynthia" : str(70),
            "alicia" : str(71),
            "melody" : str(72),
            "cursed mage" : str(74),
            "venom mage" : str(75),
            "claris" : str(76),
            "fanatics" : str(77),
            "servant of fire" : str(78),
            "energy master" : str(80),
            "beatricé" : str(81),
            "carlson" : str(82),
            "maria" : str(83),
            "arines" : str(84),
            "fist fighter" : str(85),
            "muscled warrior" : str(86),
            "rai" : str(87),
            "darkarmor lancer" : str(88),
            "leto" : str(89),
            "ron" : str(90),
            "bruno" : str(91),
            "maya" : str(92),
            "northern warrior" : str(93),
            "ax warrior" : str(94),
            "xenon" : str(97),
            "orienne" : str(98),
            "dominique" : str(99),
            "hijin" : str(100),
            "sizka" : str(101),
            "viola" : str(102),
            "ridel" : str(103),
            "guard knight" : str(104),
            "escort knight" : str(105),
            "bone destroyer" : str(106),
            "bone grinder" : str(107),
            "dark mage" : str(108),
            "illusionist" : str(109),
            "lorang" : str(110),
            "esther" : str(111),
            "flame mage" : str(112),
            "fire mage" : str(113),
            "elisé" : str(114),
            "lucrezia" : str(115),
            "zarka" : str(116),
            "anais" : str(118),
            "wester" : str(119),
            "old sage" : str(120),
            "warlock" : str(121),
            "hell" : str(122),
            "orc spearman" : str(123),
            "bugle torfin" : str(124),
            "bugle kellon" : str(125),
            "ino" : str(126),
            "allan warrior" : str(127),
            "deka" : str(128),
            "edin" : str(132),
            "siegmund" : str(133),
            "gunther" : str(134),
            "armored lancer" : str(135),
            "rogan" : str(136),
            "rené" : str(138),
            "frederica" : str(139),
            "grosa" : str(140),
            "pirate grunt" : str(141),
            "magnus" : str(142),
            "agaron" : str(143),
            "bulky pirate" : str(144),
            "kyle" : str(145),
            "ors" : str(146),
            "archmage" : str(147),
            "high wizard" : str(148),
            "troll shaman" : str(149),
            "anubis" : str(151),
            "mary" : str(152),
            "elijah" : str(153),
            "john" : str(155),
            "celia" : str(156),
            "elija" : str(157),
            "wilhelmina" : str(158),
            "ingrid" : str(160),
            "gargoyle" : str(162),
            "naja" : str(163),
            "giant" : str(165),
            "ymir" : str(171),
            "trent" : str(173),
            "orc tamer" : str(174),
            "alec" : str(177),
            "granhildr" : str(178),
            "angelica" : str(179),
            "nartas" : str(180),
            "rigenette" : str(181),
            "astrid" : str(182),
            "gnoll warrior" : str(183),
            "winterwood" : str(184),
            "refithea" : str(185),
            "mummy" : str(186),
            "imp" : str(187),
            "skeleton archer" : str(192),
            "undead beheader" : str(193),
            "wraith" : str(194),
            "devil's pawn" : str(199),
            "furious warrior" : str(202),
            "berserker" : str(203),
            "court mage" : str(204),
            "principal mage" : str(205),
            "sloan" : str(206),
            "undead soldier" : str(208),
            "octavia" : str(210),
            "glacia" : str(211),
            "frozen warrior" : str(212),
            "kozak" : str(215),
            "mora" : str(216),
            "iris" : str(217),
            "rafina" : str(218),
            "deomaron" : str(219),
            "veronia" : str(220),
            "vermont" : str(221),
            "edan" : str(222),
            "eras" : str(223),
            "daniel" : str(224),
            "apprentice warrior" : str(225),
            "mercenary trainee" : str(226),
            "asera" : str(227),
            "julie" : str(228),
            "eunice" : str(229),
            "zakan" : str(230),
            "arkan" : str(231),
            "jin" : str(232),
            "alche" : str(233),
            "michaela" : str(234),
            "gloria" : str(235),
            "garinoth" : str(236),
            "martina" : str(237),
            "camilla" : str(238),
            "brisa" : str(239),
            "varion" : str(240),
            "niya" : str(241),
            "musket geezer" : str(262),
            "mia" : str(263),
            "natalie" : str(264),
            "novice defender" : str(266),
            "bdm n-0524" : str(267),
            "dr. morgan" : str(268),
            "christina" : str(269),
            "valtor" : str(270),
            "serendia" : str(271),
            "eldora" : str(272),
            "krull" : str(273),
            "lufel" : str(274),
            "yuria" : str(275),
            "foxy" : str(276),
            "cecilia" : str(277),
            "ventana" : str(278),
            "ebony" : str(279),
            "bathory" : str(280),
            "gaius" : str(281),
            "venaka" : str(282),
            "eunrang" : str(283),
            "farrel" : str(284),
            "kellan" : str(285),
            "sabrina" : str(286),
            "jacklin" : str(287),
            "lucius" : str(288),
            "seto" : str(289),
            "asmode" : str(290),
            "velfern" : str(291),
            "mamonir" : str(292),
            "valzé" : str(293),
            "beliath" : str(294),
            "levia" : str(295),
            "seir" : str(296),
            "dalvi" : str(297),
            "vincent" : str(298),
            "chalkle" : str(299),
            "dwen" : str(300),
            "denarisa" : str(301),
            "aie" : str(302),
            "floria" : str(303),
            "barbara" : str(304),
            "zenith" : str(305),
            "kaoli" : str(306),
            "ceres" : str(307),
            "kaina" : str(308),
            "freesia" : str(309),
            "grace" : str(310),
            "hyeon wol" : str(311),
            "blaze" : str(312),
            "lydia" : str(313),
            "marron" : str(314),
            "baine" : str(330),
            "eleaneer" : str(331),
            "corette" : str(332),
            "victor" : str(333),
            "lillian" : str(334),
            "kuwik" : str(335),
            "thalos" : str(338),
            "jayden" : str(339),
            "horan" : str(340),
            "themis" : str(341),
            "aaron" : str(342),
            "leah" : str(343),
            "hanya" : str(349),
            "kaylin" : str(350),
            "karin" : str(351),
            "walya" : str(352),
            "yuri" : str(353),
            "acha" : str(354),
            "lecliss" : str(355),
            "edwin" : str(356),
            "sarubia" : str(357),
            "antonio" : str(358),
            "anastasia" : str(359),
            "dr. logic" : str(360),
            "kanna" : str(376),
            "arwen" : str(377),
            "laura" : str(378),
            "martius" : str(379),
            "naressa" : str(380),
            "charlotte" : str(381),
            "lumen" : str(382),
            "lian" : str(383),
            "ludia" : str(384),
            "eindolin" : str(385),
            "naius" : str(386),
            "taylor" : str(387),
            "ayan" : str(388),
            "stella" : str(389),
            "kry" : str(390),
            "catherine" : str(391),
            "isabel" : str(392),
            "larkis" : str(393),
            "bellasier" : str(394),
            "rimuru tempest" : str(395),
            "milim nava" : str(396),
            "benimaru" : str(397),
            "gobta" : str(398),
            "shion" : str(399)}
            
        return(mercs[merc_choice])