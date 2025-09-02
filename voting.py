"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""

candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    """Register candidates with optional metadata."""
	for candidate in args:
        	if candidate not in candidates:
            candidates[candidate] = {"votes": 0}
            # Merge optional details if given
            candidates[candidate].update(kwargs)
    	return f"Registered candidates: {list(args)}"

    pass

def cast_vote(voter_id, candidate):
    """Cast vote if voter has not voted before.
        after all the vote logic is completeted sucessfully,
        return: Vote casted for {candidate}.
    """
	if voter_id in voters:
        	return f"Voter {voter_id} has already voted!"
    	if candidate not in candidates:
        	return f"Candidate {candidate} not found!"
    
    	candidates[candidate]["votes"] += 1
    	voters.add(voter_id)
    	return f"Vote casted for {candidate}."
   
 pass

def election_result():
    """Return the winner(s)."""
	if not candidates:
        return {"winners": [], "candidates": {}}
    
    # Find max votes
    	max_votes = max(c["votes"] for c in candidates.values())
    # Collect all winners (in case of tie)
    	winners = [name for name, c in candidates.items() if c["votes"] == max_votes]
    
    	return {"winners": winners, "candidates": candidates}
    # max_votes = #add logic
    # winners = #add logic
    # return {"winners": winners, "candidates": candidates}
