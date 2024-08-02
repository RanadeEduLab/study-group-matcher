from models import Row, Column, Node, Match
import os
import pandas as pd
import numpy as np


def year_transformer(year):
    year = year.lower()
    if "transfer" in year:
        return 3
    elif "junior" in year or "senior" in year:
        return 2
    elif "sophomore" in year:
        return 1
    else:
        return 1


def gender_transformer(gender):
    if "Do not use" in gender:
        return 4
    if "Transgender" in gender or \
        "Non-binary" in gender or \
        "Gender non-conforming" in gender or \
            len(gender) > 1:
        return 0
    gender = gender[0]
    if gender == "Female":
        return 1
    elif gender == "Male":
        return 2
    elif gender != "Prefer not to answer":
        return 3


def race_transformer(race):
    if "Do not use" in race:
        return 9
    if "Black / African American" in race:
        return 0
    elif "Latino / Latinx / Chicano / Chicanx / Hispanic" in race:
        return 1
    elif "American Indian / Alaska Native" in race:
        return 2
    elif "Middle Eastern / North African" in race:
        return 3
    elif "Native Hawaiian / Pacific Islander" in race:
        return 4
    elif "Multiple races" in race:
        return 5
    elif "Asian / Asian American" in race:
        return 6
    elif "White" in race:
        return 7
    else:
        return 8


def interaction_transformer(choice):
    if "None of the above" in choice:
        return 1
    elif "Doing work separately and discussing approaches" in choice:
        return 2
    elif "Socializing / meeting new people in non-academic contexts" in choice:
        return 3
    else:
        return 4


def email_transformer(email):
    return email.lower().strip()


def course_transformer(course):
    if ("Math 1" in course):
        return 1
    elif ("Math 5" in course):
        return 2
    elif ("Physics 7" in course):
        return 3
    elif ("CS 70" in course):
        return 4
    elif ("CS 61C" in course):
        return 5
    elif ("CS 61" in course):
        return 6
    else:
        return 4
    
def location_transformer(place):
    if ("Unit 1/Unit 2/Martinez" in place):
        return 1
    elif ("Unit 3/Blackwell" in place):
        return 2
    elif ("Clark Kerr" in place):
        return 3
    elif ("Foothill/Stern/Bowles" in place):
        return 4
    elif ("Off-campus Southside (south of Bancroft Way)" in place):
        return 5
    elif ("Off-campus Downtown (east of Fulton/Oxford St.)" in place):
        return 6
    elif ("Off-campus Northside (north of Hearst Ave.)" in place):
        return 7
    elif ("N/A, I am a commuter student." in place):
        return 8
    else:
        return 9


# NOTE: Do not delete Column objects marked with is_optional=False,
#       unless you're sure you'd like to change that functionality
ROW_CONFIG = Row(
    [
        Column(
            "Email Address",
            "email",
            "email",
            is_optional=False,
            transformer=email_transformer,
        ),
        Column("First name", "first_name", "text"),
        Column("Last name", "last_name", "text"),
        Column("SID", "sid", "sid", is_optional=False),
        Column(
            "Would you like to be part of a course study group",
            "want_group",
            "text",
            transformer=lambda x: x == "Yes",
            is_optional=False,
        ),
        Column(
            "Would you like additional people to join your group",
            "additional_students",
            "text",
            transformer=lambda x: x == "Yes",
            is_optional=True,
        ),
        Column(
            "Do you already know some students in the course",
            "is_existing",
            "text",
            transformer=lambda x: x == "Yes",
            is_optional=False,
        ),
        Column(
            "2nd Group Member Berkeley Student Email",
            "groupmember2",
            "email",
            is_optional=True,
            transformer=email_transformer,
        ),
        Column(
            "3rd Group Member Berkeley Student Email",
            "groupmember3",
            "email",
            is_optional=True,
            transformer=email_transformer,
        ),
        Column(
            "4th Group Member Berkeley Student Email",
            "groupmember4",
            "email",
            is_optional=True,
            transformer=email_transformer,
        ),
        Column(
            "5th Group Member Berkeley Student Email",
            "groupmember5",
            "email",
            is_optional=True,
            transformer=email_transformer,
        ),
        Column(
            "6th Group Member Berkeley Student Email",
            "groupmember6",
            "email",
            is_optional=True,
            transformer=email_transformer,
        ),
        Column(
            "What year are you",
            "year",
            "radio",
            is_optional=False,
            transformer=year_transformer,  # Buckets years
        ),
        Column(
            "When would you like to work on homework",
            "hw_start",
            "radio",
            is_optional=False,
        ),
        Column(
            "How often would you like the group to meet",
            "interaction_freq",
            "radio",
            is_optional=False,
        ),
        Column(
            "Would you be willing to lead a group",
            "leader",
            "text",
            transformer=lambda x: x == "Yes",
            is_optional=False, 
        ),
        Column("How would you like to interact with a study group",
               "interact_types",
               "checkbox",
               is_optional=False,
               transformer=interaction_transformer
               ),
        Column(
            "What other technical classes are you currently taking",
            "taking",
            "checkbox",
            is_optional=False,
            transformer=course_transformer,
        ),
        Column("Which discussion section times",
               "disc_times_options",
               "checkbox",
               is_optional=False,
               # transformer=discussion_transformer, # NOTE: Uncomment this line if you'd like to bucket discussion times
               ),
        Column("What part of Berkeley do you live in",
               "location_options",
               "radio",
               is_optional=False,
               transformer=location_transformer,
               ),
        # Column(
        #     "Check the option that applies for you, to help us understand your programming",
        #     "programming_experience",
        #     "checkbox",
        #     is_optional=False,
        # ),
        Column(
            "May we use your demographic information",
            "use_demographic",
            "text",
            transformer=lambda x: x == "Yes",
            is_optional=False,  # Buckets years
        ),
        Column(
            "Would you prefer a study group where at least one other student",
            "prefers_dem_matching",
            "text",
            transformer=lambda x: ("Yes" in x) or (
                "Maybe" in x) or ("Indifferent" in x),
            is_optional=False
        ),
        Column(
            "Which of these options best describes your race?",
            "race",
            "checkbox",
            is_optional=True,
            transformer=race_transformer,
        ),
        Column(
            "How do you self-identify?",
            "gender",
            "checkbox",
            is_optional=True,
            transformer=gender_transformer,
        ),
        Column(
            "Are you an international student",
            "international",
            "text",
            is_optional=True,
            transformer=lambda x: x == "Yes",
        ),
        Column(                       # TODO: comment in this Column if you wish to pregroup students
            "pregroup_partner",
            "pregroup_partner",
            "text",
            is_optional=True,
            transformer=email_transformer,
        ),
        Column(                       # TODO: comment in this Column if you wish to pregroup students
            "pregroup_partner2",
            "pregroup_partner2",
            "text",
            is_optional=True,
            transformer=email_transformer,
        ),
    ]
)

CONSTRAINTS = {

    "Partition": ["year", "location_options", "hw_start", "interaction_freq", "use_demographic"],
    "Existing": {
        "type": "explicit_keys",
        "flag": "is_existing",
        "id_key": "email",
        "flag_addtl": "additional_students",
        "data": ["groupmember2", "groupmember3", "groupmember4", "groupmember5", "groupmember6"],
    },

    "Best-effort": [
        ["hw_start", "interaction_freq", "interact_types", "taking",
            "international", "use_demographic", "disc_times_options", "race"],
        [2, 1, 1, .5, .5, 1, 1, 0.25, 1, 2, 3],
    ],  # column ID's for features followed by weights
}

MIN_GROUP_SIZE = 3
MAX_GROUP_SIZE = 7
MIN_PARTITION_SIZE = 4
PREGROUP_PARTNERS = True
ENFORCE_PREGROUP = True

#####
# Below this point are pre- and post-processing functions for the grouping algorithm.
# Feel free to customize these to your liking, but functionality can be most easily controlled
# by changing the ROW_CONFIG, the CONSTRAINTS, and the other constants above.
#####


def pre_process_csv(csv_file):
    """
    Processes the input csv, changes it, and saves a new version to a different csv,
    returning the string path to the new processed csv
    """
    if PREGROUP_PARTNERS:
        MATCH_WITH_OTHERS_Q = 'Would you like additional people to join your group? (Only if your current group is smaller than 4)'
        PARTNER_2_Q = '2nd Group Member Berkeley Student Email (must be @berkeley.edu)'
        PARTNER_3_Q = '3rd Group Member Berkeley Student Email (must be @berkeley.edu)'
        PARTNER_4_Q = None
        # this is a column that will be added by this script
        PREGROUP_COL = 'pregroup_partner'
        # this is a column that will be added by this script
        PREGROUP_COL2 = 'pregroup_partner2'
        EMAIL_Q = 'Email Address'
 
        with open(csv_file, 'rb') as f:
            df = pd.read_csv(f, dtype=str)

        join_on = df[[EMAIL_Q, PARTNER_2_Q]].rename(
            columns={EMAIL_Q: 'p2', PARTNER_2_Q: 'p2_choice'})
        ungrouped_df = df[[EMAIL_Q, PARTNER_2_Q]].merge(right=join_on,
                                                        how='left',
                                                        left_on=PARTNER_2_Q, right_on='p2')

        # don't pregroup if the other person didn't list them back (unless the other person didn't indicate anyone)
        ungrouped_df = ungrouped_df[ungrouped_df[EMAIL_Q] ==
                                    ungrouped_df['p2_choice']][[EMAIL_Q, PARTNER_2_Q]]
        ungrouped = ~df[EMAIL_Q].isin(ungrouped_df[EMAIL_Q])

        # don't pregroup if someone listed a partner who did not send in a response
        partner_isnotin_emails = ~df[PARTNER_2_Q].isin(df[EMAIL_Q])

        # mask with above criteria, and don't pregroup if someone doesn't wish to be matched with others

        pregroup_col = df[PARTNER_2_Q].mask(partner_isnotin_emails, '')\
            .mask(ungrouped, '')
        if not ENFORCE_PREGROUP and (MATCH_WITH_OTHERS_Q is not None):
            pregroup_col = pregroup_col.mask(
                df[MATCH_WITH_OTHERS_Q] != 'Yes', '')
        # insert a new column for "pregroup_partner"

        if PARTNER_3_Q != None:

            join_on = df[[EMAIL_Q, PARTNER_3_Q]].rename(
                columns={EMAIL_Q: 'p3', PARTNER_3_Q: 'p3_choice'})
            ungrouped_df = df[[EMAIL_Q, PARTNER_3_Q]].merge(right=join_on,
                                                            how='left',
                                                            left_on=PARTNER_3_Q, right_on='p3')

            # don't pregroup if the other person didn't list them back (unless the other person didn't indicate anyone)
            ungrouped_df = ungrouped_df[ungrouped_df[EMAIL_Q] ==
                                        ungrouped_df['p3_choice']][[EMAIL_Q, PARTNER_3_Q]]
            ungrouped = ~df[EMAIL_Q].isin(ungrouped_df[EMAIL_Q])

            # don't pregroup if someone listed a partner who did not send in a response
            partner_isnotin_emails = ~df[PARTNER_3_Q].isin(df[EMAIL_Q])

            # mask with above criteria, and don't pregroup if someone doesn't wish to be matched with others

            pregroup_col2 = df[PARTNER_3_Q].mask(partner_isnotin_emails, '')\
                .mask(ungrouped, '')
            if not ENFORCE_PREGROUP and (MATCH_WITH_OTHERS_Q is not None):
                pregroup_col2 = pregroup_col2.mask(
                    df[MATCH_WITH_OTHERS_Q] != 'Yes', '')
        else:
            pregroup_col2 = df[PARTNER_2_Q].mask(
                np.ones(df[PARTNER_2_Q].shape) == 1, '')

        if PARTNER_4_Q != None:

            pregrouped_with_4_errored = df[PARTNER_4_Q].mask(
                df[MATCH_WITH_OTHERS_Q] != 'Yes', '')
            if (pregrouped_with_4_errored != '').sum() > 0:
                print("\nThe following students will not be grouped correctly, due to \
                    someone listing them as a 4th group member while asking to be matched with additional students")
                print(pregrouped_with_4_errored)

        df.insert(len(df.columns), PREGROUP_COL, pregroup_col)
        df.insert(len(df.columns), PREGROUP_COL2, pregroup_col2)
        print(PREGROUP_COL2)
        proc_csv_name = csv_file[:-4]+'_proc.csv'
        with open(proc_csv_name, 'w') as f:
            df.to_csv(proc_csv_name, index=False)

    else:
        proc_csv_name = csv_file

    with open(proc_csv_name, 'r',) as f:
        df = pd.read_csv(f, dtype=str)

    proc_csv_name = csv_file[:-4]+'_proc.csv'

    # Do consent preprocessing on demographics question

    use_demographic = "May we use your demographic information to improve your course study group match for this semester?"
    prefer_demographic = "Would you prefer a study group where at least one other student shared a common identity with you?"
    race = "Which of these options best describes your race? (Check all that apply)"
    gender = "How do you self-identify? (Check all that apply)"
    international = "Are you an international student (primarily residing outside the US)?"

    condition = np.logical_and(
        df[use_demographic] == "Yes",
        np.isin(df[prefer_demographic], ["Yes", "Maybe", "Indifferent"]),

    )

    df[race] = np.where(condition, df[race], "Do not use")
    df[gender] = np.where(condition, df[gender], "Do not use")
    df[international] = np.where(condition, df[international], "Do not use")
    with open(proc_csv_name, 'w') as f:
        df.to_csv(f, index=False)
    return proc_csv_name


pregrouped = {
}


def pregroup_nodes(nodes: list) -> list:
    # Only match students who want a group
    filtered = [node for node in nodes if node.props[0]["want_group"]]
    by_email = {}
    for node in filtered:
        by_email[node.props[0]["email"]] = node
    filtered = list(by_email.values())
    # return filtered

    # Now pre-pair students who want to be pre-paired
    if PREGROUP_PARTNERS:
        indices_to_remove = []
        paired = []
        for (i, node) in enumerate(filtered):
            partner = by_email.get(node.props[0]["pregroup_partner"], None)
            if partner and i not in indices_to_remove:
                found = filtered.index(partner)
                if found is None or found == i:
                    continue
                assert found is not None and found != i
                indices_to_remove.append(i)
                indices_to_remove.append(found)

                # Check if has second partner listed
                partner2 = by_email.get(
                    node.props[0]["pregroup_partner2"], None)
                if partner2:
                    found2 = filtered.index(partner2)
                    assert found2 is not None and found2 != i
                    indices_to_remove.append(found2)
                    print(
                        i,
                        found,
                        found2,
                        node.props[0]["pregroup_partner"],
                        partner.props[0]["email"],
                        node.props[0]["pregroup_partner2"],
                        partner2.props[0]["email"],
                    )
                    paired.append(node)
                    pregrouped[node.props[0]["email"]] = [partner, partner2]
                else:
                    print(
                        i,
                        found,
                        node.props[0]["pregroup_partner"],
                        partner.props[0]["email"],
                    )
                    paired.append(node)
                    pregrouped[node.props[0]["email"]] = [partner]

        print(
            "People who entered a partner who did not fill out the form:",
            [
                (i, n.props[0]["pregroup_partner"])
                for i, n in enumerate(filtered)
                if i not in indices_to_remove and n.props[0]["pregroup_partner"]
            ],
        )
        for i, n in enumerate(filtered):
            if i not in indices_to_remove and n.props[0]["pregroup_partner"]:
                n.props[0][
                    "pregroup_partner"
                ] += " (this person did not fill out the form or incorrect email!)"
        filtered = [filtered[i]
                    for i in range(len(filtered)) if i not in indices_to_remove]
        filtered += paired
    print(PREGROUP_PARTNERS, filtered)
    return filtered


def batch(arr, n=2):
    ret = []
    if not len(arr) // n:
        return [arr]
    for i in range(len(arr) // n):
        at = arr[i * n: i * n + n]
        if i + 1 >= len(arr) // n:
            at = arr[i * n:]
        ret.append(at)
    return ret


def group_races(arr, n=2):
    by_race = {}
    for node in arr:
        currnode_race = node["race"]
        by_race[currnode_race] = by_race.get(currnode_race, []) + [node]
    for race in list(by_race.keys()):
        members = by_race[race]
        if len(members) > 1:
            yield from batch(members, n=n)
            del by_race[race]
    yield from batch(sum(by_race.values(), []), n=n)


def group_genders(arr, n=2):
    by_gender = {}
    for node in arr:
        by_gender[node["gender"]] = by_gender.get(node["gender"], []) + [node]
    yield from group_races(by_gender.get(1, []), n=n)
    if 1 in by_gender:
        del by_gender[1]
    yield from group_races(sum(list(by_gender.values()), []), n=n)


def postprocess_partitions(subgroups: list) -> list:
    # Black
    # Indigenous Native American / Pacific Islander
    # Cis Female
    # Hispanic
    # All non-male/female genders
    # Race: 2-6 are underrepresented
    # Gender: not male == underrepresented

    for (group_num, group) in enumerate(subgroups):
        new_nodes = []
        for at in group_genders(sum((node.props for node in group[2]), [])):
            merged = Node(at, size=len(at), assigned=True)
            new_nodes.append(merged)
        subgroups[group_num] = (group[0], group[1], new_nodes, group[3])

    return subgroups


def is_black(props):
    return props["race"] is not None and (props["race"] == 0)


def is_hispanic(props):
    return props["race"] is not None and (props["race"] == 1)


def is_indigenous(props):
    return props["race"] is not None and (props["race"] == 2)


def is_female(props):
    return props["gender"] is not None and (props["gender"] == 0)


def is_nonmf(props):
    return props["gender"] is not None and (props["gender"] not in (0, 1))


def is_underrepresented(props):
    return (
        props["race"] is not None
        and props["race"] <= 3
        or ((props["gender"] is not None) and props["gender"] != 1)
    )


def post_processing(matches: list):
    from collections import Counter

    def describe_group(match: Match):
        race_map = {
            0: "Black",
            1: "Latinx",
            2: "Indigenous",
            3: "MENA",
            4: "Native Hawaiian",
            5: "Multiple Races",
            6: "Asian",
            7: "White",
            8: "DTS",
            9: "Do not use",
            None: "DTS",
        }

        gender_map = {0: "Female", 1: "Male", 2: "Non-M/F",
                      3: "DTS", None: "DTS", 4: "Do not"}

        return (
            ", ".join(
                [
                    (race_map[x.get("race", 8)] + " " +
                     gender_map[x.get("gender", 3)])
                    for x in match.node.props
                ]
            )
            + " ("
            + (
                ", ".join(f"{x[0]}: {x[1]}" for x in match.path)
                if isinstance(match.path, tuple)
                else match.path
            )
            + ")"
        )

    by_size = {}
    for match in matches:
        if match.source == "existing":
            continue
        by_size[match.size] = by_size.get(match.size, []) + [match]

    if 2 in by_size: 
        matches = [match for match in matches if match not in by_size[2]]
        for arr in batch(by_size[2], n=2):
            props = sum((x.node.props for x in arr), [])
            node = Node(props, size=(len(arr) * 2), assigned=True)
            matches.append(
                Match(node=node, source="path", path="(manually fixed)"))

    existing_singletons = []
    for match in matches:
        if match.source != "existing":
            continue
        if match.size == 1:
            existing_singletons.append(match)
    print(f"Singleton count: {len(existing_singletons)}")
    matches = [match for match in matches if match not in existing_singletons]
    print("DEBUG: props and singletons", [
          match.node.props for match in existing_singletons])
    for props in group_genders(
        [match.node.props[0] for match in existing_singletons], n=3
    ):
        node_size = len(props)
        if node_size == 1:
            print(props[0])
        node = Node(props, size=node_size, assigned=True)
        matches.append(
            Match(
                node=node,
                source="path",
                path="(singleton manually fixed)",
            )
        )

    leader_counts = []
    for match in matches:
        print("******these are leader details*******")
        total_leaders = 0
        found_leader = False
        print(match.node.can_split)
        for person in match.node.props:
            leader = person["leader"]
            if leader:
                total_leaders += 1
        leader_counts.append(total_leaders)
    print("leader counts", leader_counts)


    black_groups = []
    for match in matches:
        if any(is_black(x) for x in match.node.props):
            black_groups.append(match)
    black_groups = sorted(black_groups, key=lambda x: x.size, reverse=True)
    for i in range(len(black_groups) // 2):
        member = [x for x in black_groups[i].node.props if is_black(x)][0]
        if is_female(member):
            continue
        black_groups[i].node.size -= 1
        black_groups[i].node.props.remove(member)
        j = i + len(black_groups) // 2
        black_groups[j].node.size += 1
        black_groups[j].node.props.append(member)

    # Pair up hispanic students
    hispanic_groups = []
    for match in matches:
        if match.source == "existing" or match.path == "(singleton manually fixed)":
            continue
        num_hispanic_students = 0
        for x in match.node.props:
            if is_hispanic(x):
                num_hispanic_students = num_hispanic_students + 1
        if num_hispanic_students == 1:
            hispanic_groups.append(match)
    hispanic_groups = sorted(
        hispanic_groups, key=lambda x: x.size, reverse=True)
    for i in range(len(hispanic_groups) // 2):
        member = [
            x for x in hispanic_groups[i].node.props if is_hispanic(x)][0]
        hispanic_groups[i].node.size -= 1
        hispanic_groups[i].node.props.remove(member)
        hispanic_groups[i].path = "(hispanic modification singletons - 1)"
        j = i + len(hispanic_groups) // 2
        hispanic_groups[j].node.size += 1
        hispanic_groups[j].node.props.append(member)
        hispanic_groups[j].path = "(hispanic modification singletons + 1)"

    total_num = 0
    minority_groups = [
        ("Black", is_black),
        ("Hispanic", is_hispanic),
        ("Indigenous", is_indigenous),
        ("female", is_female),
        ("non-mf", is_nonmf),
        ("underrepresented", is_underrepresented),
    ]
    for (minority_group, minority_fn) in minority_groups:
        fractions, lengths = {}, {}
        for match in matches:
            if match.source == "existing":
                continue
            num_minority = sum(1 for x in match.node.props if minority_fn(x))
            group_desc = describe_group(match)
            if num_minority > 0:
                fractions[num_minority] = fractions.get(
                    num_minority, []) + [group_desc]
                lengths[num_minority] = lengths.get(
                    num_minority, 0) + match.size

        counter = fractions
        if not counter:
            print(f"No {minority_group} members found, skipping.")
            continue

        print("")
        print(
            f"For all {len(sum(counter.values(), []))} groups ({sum(lengths.values())} students) with {minority_group} member(s):"
        )
        for k in sorted(counter.keys()):
            print(
                f"\t{len(counter[k]) / len(sum(counter.values(), [])):.1%} ({len(counter[k])} groups) representing {lengths[k] / sum(lengths.values()):.1%} of {minority_group} students had {k} {minority_group} member(s):"
            )
            print("******")
            print("\n".join(counter[k]))
            print("******")

    for match in matches:
        for person in match.node.props:
            if person["email"] in pregrouped:
                for new_mem in pregrouped[person["email"]]:
                    match.node += new_mem

    out = []
    for match in matches:
        added = [x["partner"] for x in match.node.props if "partner" in x]
        match.node.props += added
        print("added:", match)
    match_depths = {1: 0, 2: 0, 3: 0, 4: 0}

    for (i, match) in enumerate(matches):

        for person in match.node.props:

            out.append(
                {
                    "group_num": i,
                    "email": person["email"],
                    "sid": person["sid"],
                    "first": person["first_name"],
                    "last": person["last_name"],
                    "incoming_partners": person.get("incoming_partners", "N/A"),
                    "outgoing_partners": person.get("outgoing_partners", "N/A"),
                    "year": person["year"],
                    "freq": person["interaction_freq"],
                    "race": person["race"],
                    "gender": person["gender"],
                    "had existing": person["is_existing"],
                    "is_leader": person["leader"],
                    "location": person["location_options"],
                    "pregroup_partner": person.get("pregroup_partner", "N/A"),
                    "pregroup_partner2": person.get("pregroup_partner2", "N/A")
                }
            )

    print("*** Match Stats ***")
    print(match_depths)
    print("***")
    df = pd.DataFrame(out)
    out_fname = "out-private.csv"
    out_fname_format = "out-private-{}.csv"
    if os.path.isfile(out_fname):
        i = 2
        while os.path.isfile(out_fname_format.format(i)):
            i += 1
        out_fname = out_fname_format.format(i)
    print(f"Outputting {len(out)} students to '{out_fname}'.")
    df.to_csv(out_fname, encoding="utf-8", index=False)
